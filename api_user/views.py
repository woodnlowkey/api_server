from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.db.models import Q
from django.core.paginator import Paginator

from .serializers import IngredientSerializer, SandwichSerializer
from .models import Ingredient, Sandwich


class IngredientView(APIView):
    
    # 'ing/' 로 'post' 하는 경우 = 재료를 추가합니다.
    def post(self, request):
        # Request의 data를 IngredientSerializer로 변환
        ingredient_serializer = IngredientSerializer(data=request.data) 
        # 유효한 요청을 확인
        if ingredient_serializer.is_valid():
            # IngredientSerializer의 유효성 검사를 한 뒤 DB에 저장
            ingredient_serializer.save() 
            # client에게 JSON response 전달
            return Response(ingredient_serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 유효한 요청이 아닌 경우 IngredientSerializer의 에러메시지를 전달
            return Response(ingredient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 'ing/' 로 'get' 하는 경우 = 재료 목록을 조회합니다.
    # 'ing/ing_id' 로 'get' 하는 경우 = 재료를 조회합니다.
    def get(self, request, **kwargs):
        categories = ['bread', 'topping', 'cheese', 'sauce']
        # 모든 재료를 불러옵니다. (삭제된 데이터 제외)
        ingredient_queryset = Ingredient.objects.exclude(deleted_data=True).distinct()
        ing_id = kwargs.get('ing_id')
        querysets = {}
        # 재료가 있고 id가 요청에 없는 경우
        if ingredient_queryset and ing_id is None:
            # 빵, 토핑, 치즈, 소스로 나누어 딕셔너리로 전달
            for cat in categories:
                # 각 카테고리별로 쿼리셋을 정의하여
                queryset = ingredient_queryset.filter(Q(category=cat)).distinct()
                # IngredientSerializer를 이용한 쿼리셋 전달
                queryset_serializer = IngredientSerializer(queryset, many=True)
                # 카테고리명을 키값으로 하는 딕셔너리
                querysets[cat] = queryset_serializer.data
            return Response(querysets, status=status.HTTP_200_OK)
        # id가 요청에 있고 해당하는 아이디의 재료가 있는 경우(예외처리를 위한 필터링)
        elif ing_id and ingredient_queryset.filter(Q(id=ing_id)):
            # id에 해당하는 재료의 정보를 불러온다.
            search_ing_queryset = ingredient_queryset.get(id=ing_id)
            # IngredientSerializer를 이용한 쿼리셋 전달
            ing_serializer = IngredientSerializer(search_ing_queryset) 
            # client에게 JSON response 전달
            return Response(ing_serializer.data, status=status.HTTP_200_OK)
        # 그 외
        else:
            return Response('No Data', status=status.HTTP_400_BAD_REQUEST)
    
    # 'ing/ing_id/' 로 'put' 하는 경우 = 재료를 수정합니다.
    def put(self, request, **kwargs):
        ing_id = kwargs.get('ing_id')
        # id가 요청에 없는 경우
        if ing_id is None:
            return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
        # 그 외
        else:
            # 모든 재료를 불러옵니다. (삭제된 데이터 제외)
            ingredient_queryset = Ingredient.objects.exclude(deleted_data=True).distinct()
            # 해당하는 아이디의 재료가 있는 경우
            if ingredient_queryset.filter(Q(id=ing_id)):
                # 재료를 불러옵니다.
                search_ing_queryset = Ingredient.objects.get(id=ing_id)
                update_ing_serializer = IngredientSerializer(search_ing_queryset, data=request.data)
                # 유효한 요청을 확인
                if update_ing_serializer.is_valid():
                    # IngredientSerializer의 유효성 검사를 한 뒤 DB에 저장
                    update_ing_serializer.save()
                    # client에게 JSON response 전달
                    return Response(update_ing_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
            # 그 외
            else:
                return Response('No Data', status=status.HTTP_400_BAD_REQUEST)
    
    # 'ing/ing_id/' 로 'delete' 하는 경우 = 재료를 삭제합니다.
    def delete(self, request, **kwargs):
        ing_id = kwargs.get('ing_id')
        # id가 요청에 없는 경우
        if ing_id is None:
            return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
        else:
            # 모든 재료를 불러옵니다. (삭제된 데이터 제외)
            ingredient_queryset = Ingredient.objects.exclude(deleted_data=True).distinct()
            # 해당하는 아이디의 재료가 있는 경우
            if ingredient_queryset.filter(Q(id=ing_id)):
                # 재료를 불러옵니다.
                search_ing_queryset = Ingredient.objects.get(id=ing_id)
                # 해당 재료를 수정하고 저장
                deleted = {'deleted':{'category':search_ing_queryset.category, 'name':search_ing_queryset.name}}
                search_ing_queryset.deleted_data = True
                search_ing_queryset.save()
                # 삭제한 빵의 이름을 알림
                return Response(deleted, status=status.HTTP_200_OK)
            # 그 외
            else:
                return Response('No Data', status=status.HTTP_400_BAD_REQUEST)

# input = QueryDict.copy()
# output = int
def total_price(categories, ingredients):
    valid = True
    price = 0
    for cat in categories:
        # 카테고리에 해당하는 키가 있는 경우
        if ingredients.get(cat, default=None):
            # 재료를 불러옵니다.
            ingredient_object = Ingredient.objects.get(id=ingredients[cat])
            # 재료의 카테고리와 일치하는지, 재고가 있는지 확인
            if ingredient_object.category[:5] == cat[:5] and ingredient_object.stock:
                # 재료 가격의 합
                price += ingredient_object.price
            # 일치하지 않거나 재고가 없는 경우
            else:
                # 유효하지 않음 설정
                valid = False
                break
    return valid, price

class SandwichView(APIView):

    # 'san/' 로 'post' 하는 경우 = 샌드위치를 추가합니다.
    def post(self, request):
        categories = ['bread', 'topping', 'topping2', 'cheese', 'sauce', 'sauce2']
        # 가격을 설정하기 위해 복사
        ingredients = request.data.copy()
        # 별도의 함수를 이용하여 가격을 설정, 재고를 확인합니다.
        valid, price = total_price(categories, ingredients)
        ingredients['price'] = price
        # 모든 아이디가 유효한 경우
        if valid:
            # Request의 data를 SandwichSerializer로 변환
            sandwich_serializer = SandwichSerializer(data=ingredients)
            # 유효한 요청을 확인
            if sandwich_serializer.is_valid():
                # IngredientSerializer의 유효성 검사를 한 뒤 DB에 저장
                sandwich_serializer.save()
                # 재료의 재고 -1, 저장
                for cat in categories:
                    # 카테고리에 해당하는 키가 있는 경우
                    if ingredients.get(cat, default=None):
                        ingredient_object = Ingredient.objects.get(id=ingredients[cat])
                        ingredient_object.stock -= 1
                        ingredient_object.save()
                # client에게 JSON response 전달
                return Response(sandwich_serializer.data, status=status.HTTP_201_CREATED)
            # 그 외
            else:
                # 유효한 요청이 아닌 경우 IngredientSerializer의 에러메시지를 전달
                return Response(sandwich_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 그 외
        else:
            return Response('Invalid Ingredient ID', status=status.HTTP_400_BAD_REQUEST)
    
    # 'san/' 로 'get' 하는 경우 = 샌드위치 목록을 조회합니다.
    # 'san/san_id' 로 'get' 하는 경우 = 샌드위치의 상세 정보를 조회합니다.
    def get(self, request, **kwargs):
        san_id = kwargs.get('san_id')
        san_kw = kwargs.get('san_kw')
        page = kwargs.get('page', '1')
        san_upper = kwargs.get('san_upper')
        san_lower = kwargs.get('san_lower')
        # id가 요청에 있는 지 확인
        if san_id is None:
            # 모든 sandwich의 정보를 불러옵니다.
            sandwich_queryset = Sandwich.objects.exclude(deleted_data=True).distinct()
            # 재료 검색 요청이 있는지 확인
            if san_kw:
                # 해당하는 재료를 사용한 샌드위치 필터링
                sandwich_queryset = sandwich_queryset.filter(
                    Q(bread__id__icontains=san_kw) | Q(topping__id__icontains=san_kw) |
                    Q(topping2__id__icontains=san_kw) | Q(cheese__id__icontains=san_kw) |
                    Q(sauce__id__icontains=san_kw) | Q(sauce2__id__icontains=san_kw)
                ).distinct()
            # 가격 검색 요청이 있는지 확인
            if san_upper or san_lower:
                # 이상, 이하의 값이 모두 있는 경우
                if san_upper and san_lower:
                    # 사이 값
                    sandwich_queryset = sandwich_queryset.filter(
                        Q(price__range = (san_upper, san_lower))
                    ).distinct()
                # 그 외
                elif san_upper:
                    sandwich_queryset = sandwich_queryset.filter(
                        Q(price__gte = san_upper)
                    ).distinct()
                else:
                    sandwich_queryset = sandwich_queryset.filter(
                        Q(price__lte = san_lower)
                    ).distinct()
                # 가격 순으로 정렬
                sandwich_queryset = sandwich_queryset.order_by('price')
            # paginator 활용 pagination
            paginator = Paginator(sandwich_queryset, 10)
            sandwich_queryset_serializer = SandwichSerializer(paginator.get_page(page), many=True)
            return Response(sandwich_queryset_serializer.data, status=status.HTTP_200_OK)
        # id가 요청에 있는 경우
        else:
            # id에 해당하는 sandwich의 정보를 불러옵니다.
            sandwich = Sandwich.objects.get(id=san_id)
            if sandwich.deleted_data:
                san_id = f'{san_id}-Deleted Sandwich'
            # 상세 정보 가져오기
            ingredient_objects = {}
            categories = {
                'bread':sandwich.bread_id, 'topping':sandwich.topping_id, 
                'topping2':sandwich.topping2_id, 'cheese':sandwich.cheese_id, 
                'sauce':sandwich.sauce_id, 'sauce2':sandwich.sauce2_id
            }
            for category, category_id in categories.items():
                # 사용한 재료만 가져오기
                if category_id:
                    ingredient_objects[category] = Ingredient.objects.get(id=category_id)
            # 샌드위치 가격 재설정
            sandwich.price = sum([ingredient.price for ingredient in ingredient_objects.values()])
            sandwich.save()
            # 빵, 토핑, 치즈, 소스의 이름, 재고, 가격 정보 제공
            return Response(
                    {'id':san_id, 'price':sandwich.price, 
                    'ingredients':[{
                        'category':f'{category}', 'name':ingredient.name, 
                        'stock':ingredient.stock, 'price':ingredient.price, 
                        'is_deleted':ingredient.deleted_data
                        } for category, ingredient in ingredient_objects.items()]
                    }, 
                    status=status.HTTP_200_OK)
    
    # # 'ing/ing_id/' 로 'put' 하는 경우 = 재료를 수정합니다.
    # def put(self, request, **kwargs):
    #     ing_id = kwargs.get('ing_id')
    #     # id가 요청에 없는 경우
    #     if ing_id is None:
    #         return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
    #     # 그 외
    #     else:
    #         # 모든 재료를 불러옵니다. (삭제된 데이터 제외)
    #         ingredient_queryset = Ingredient.objects.exclude(deleted_data=True).distinct()
    #         # 해당하는 아이디의 재료가 있는 경우
    #         if ingredient_queryset.filter(Q(id=ing_id)):
    #             # 재료를 불러옵니다.
    #             search_ing_queryset = Ingredient.objects.get(id=ing_id)
    #             update_ing_serializer = IngredientSerializer(search_ing_queryset, data=request.data)
    #             # 유효한 요청을 확인
    #             if update_ing_serializer.is_valid():
    #                 # IngredientSerializer의 유효성 검사를 한 뒤 DB에 저장
    #                 update_ing_serializer.save()
    #                 # client에게 JSON response 전달
    #                 return Response(update_ing_serializer.data, status=status.HTTP_200_OK)
    #             else:
    #                 return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
    #         # 그 외
    #         else:
    #             return Response('No Data', status=status.HTTP_400_BAD_REQUEST)
    
    # 'san/san_id/' 로 'delete' 하는 경우 = 샌드위치를 삭제합니다.
    def delete(self, request, **kwargs):
        san_id = kwargs.get('san_id')
        # id가 요청에 있는 지 확인
        if san_id is None:
            return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
        # id가 요청에 있는 경우
        else:
            sandwich = Sandwich.objects.get(id=san_id)
            if sandwich.deleted_data:
                return Response('Deleted Sandwich', status=status.HTTP_400_BAD_REQUEST)
            # 상세 정보 가져오기
            ingredient_objects = {}
            categories = {
                'bread':sandwich.bread_id, 'topping':sandwich.topping_id, 
                'topping2':sandwich.topping2_id, 'cheese':sandwich.cheese_id, 
                'sauce':sandwich.sauce_id, 'sauce2':sandwich.sauce2_id
            }
            for category, category_id in categories.items():
                # 사용한 재료만 가져오기
                if category_id:
                    ingredient_objects[category] = Ingredient.objects.get(id=category_id)
            for ingredient in ingredient_objects.values():
                # 재료 되돌리기
                ingredient.stock += 1
                ingredient.save()
            sandwich.deleted_data = True
            sandwich.save()
            # 삭제한 샌드위치의 재료 목록과 총 가격
            return Response(
                    {'id':san_id, 'price':sandwich.price, 
                    'ingredients':[{
                        'category':f'{category}', 'name':ingredient.name, 
                        'stock':ingredient.stock, 'price':ingredient.price, 
                        'is_deleted':ingredient.deleted_data
                        } for category, ingredient in ingredient_objects.items()]
                    }, 
                    status=status.HTTP_200_OK)