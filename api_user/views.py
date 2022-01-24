from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BreadSerializer, ToppingSerializer, CheeseSerializer, SauceSerializer, SandwichSerializer
from rest_framework import status
from .models import Bread, Topping, Cheese, Sauce, Sandwich
from django.core.paginator import Paginator
from django.db.models import Q

class BreadView(APIView):
    # 'bread/' 로 'post' 하는 경우 = 빵을 추가합니다.
    def post(self, request):
        bread_serializer = BreadSerializer(data=request.data) # Request의 data를 BreadSerializer로 변환
        # 유효한 요청을 확인
        if bread_serializer.is_valid():
            bread_serializer.save() # BreadSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(bread_serializer.data, status=status.HTTP_201_CREATED) # client에게 JSON response 전달
        else:
            return Response(bread_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 'bread/' 로 'get' 하는 경우 = 빵 목록을 조회합니다.
    # 'bread/bread_id' 로 'get' 하는 경우 = 빵을 조회합니다.
    def get(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('bread_id') is None:
            bread_queryset = Bread.objects.all() # 모든 bread의 정보를 불러온다.
            bread_queryset = bread_queryset.filter(Q(existence=True)).distinct()
            bread_queryset_serializer = BreadSerializer(bread_queryset, many=True)
            return Response(bread_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            bread_id = kwargs.get('bread_id')
            bread_queryset = Bread.objects.get(id=bread_id)
            if bread_queryset.existence:
                bread_serializer = BreadSerializer(bread_queryset) # id에 해당하는 bread의 정보를 불러온다.
                return Response(bread_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'bread/bread_id' 로 'put' 하는 경우 = 빵을 수정합니다.
    def put(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('bread_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            bread_id = kwargs.get('bread_id')
            bread_object = Bread.objects.get(id=bread_id)
            if bread_object.existence:
                update_bread_serializer = BreadSerializer(bread_object, data=request.data)
                # 유효한 요청을 확인
                if update_bread_serializer.is_valid():
                    update_bread_serializer.save()
                    return Response(update_bread_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'bread/bread_id' 로 'delete' 하는 경우 = 빵을 삭제합니다.
    def delete(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('bread_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            bread_id = kwargs.get('bread_id')
            bread_object = Bread.objects.get(id=bread_id)
            if bread_object.existence:
                bread_name = bread_object.name
                bread_object.existence = False
                bread_object.save()
                # 삭제한 빵의 이름을 알림
                return Response(f"{bread_name} has been deleted", status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)

class ToppingView(APIView):
    # 'topping/' 로 'post' 하는 경우 = 토핑을 추가합니다.
    def post(self, request):
        topping_serializer = ToppingSerializer(data=request.data) # Request의 data를 ToppingSerializer로 변환
        # 유효한 요청을 확인
        if topping_serializer.is_valid():
            topping_serializer.save() # ToppingSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(topping_serializer.data, status=status.HTTP_201_CREATED) # client에게 JSON response 전달
        else:
            return Response(topping_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 'topping/' 로 'get' 하는 경우 = 토핑 목록을 조회합니다.
    # 'topping/topping_id' 로 'get' 하는 경우 = 토핑을 조회합니다.
    def get(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('topping_id') is None:
            topping_queryset = Topping.objects.all() # 모든 topping의 정보를 불러온다.
            topping_queryset = topping_queryset.filter(Q(existence=True)).distinct()
            topping_queryset_serializer = ToppingSerializer(topping_queryset, many=True)
            return Response(topping_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            topping_id = kwargs.get('topping_id')
            topping_queryset = Topping.objects.get(id=topping_id)
            if topping_queryset.existence:
                topping_serializer = ToppingSerializer(topping_queryset) # id에 해당하는 topping의 정보를 불러온다.
                return Response(topping_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'topping/topping_id' 로 'put' 하는 경우 = 토핑을 수정합니다.
    def put(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('topping_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            topping_id = kwargs.get('topping_id')
            topping_object = Topping.objects.get(id=topping_id)
            if topping_object.existence:
                update_topping_serializer = ToppingSerializer(topping_object, data=request.data)
                # 유효한 요청을 확인
                if update_topping_serializer.is_valid():
                    update_topping_serializer.save()
                    return Response(update_topping_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'topping/topping_id' 로 'delete' 하는 경우 = 토핑을 삭제합니다.
    def delete(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('topping_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            topping_id = kwargs.get('topping_id')
            topping_object = Topping.objects.get(id=topping_id)
            if topping_object.existence:
                topping_name = topping_object.name
                topping_object.existence = False
                topping_object.save()
                # 삭제한 토핑의 이름을 알림
                return Response(f"{topping_name} has been deleted", status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)

class CheeseView(APIView):
    # 'cheese/' 로 'post' 하는 경우 = 치즈를 추가합니다.
    def post(self, request):
        cheese_serializer = CheeseSerializer(data=request.data) # Request의 data를 CheeseSerializer로 변환
        # 유효한 요청을 확인
        if cheese_serializer.is_valid():
            cheese_serializer.save() # CheeseSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(cheese_serializer.data, status=status.HTTP_201_CREATED) # client에게 JSON response 전달
        else:
            return Response(cheese_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 'cheese/' 로 'get' 하는 경우 = 치즈 목록을 조회합니다.
    # 'cheese/cheese_id' 로 'get' 하는 경우 = 치즈를 조회합니다.
    def get(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('cheese_id') is None:
            cheese_queryset = Cheese.objects.all() # 모든 cheese의 정보를 불러온다.
            cheese_queryset = cheese_queryset.filter(Q(existence=True)).distinct()
            cheese_queryset_serializer = CheeseSerializer(cheese_queryset, many=True)
            return Response(cheese_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            cheese_id = kwargs.get('cheese_id')
            cheese_queryset = Cheese.objects.get(id=cheese_id)
            if cheese_queryset.existence:
                cheese_serializer = CheeseSerializer(cheese_queryset) # id에 해당하는 cheese의 정보를 불러온다.
                return Response(cheese_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'cheese/cheese_id' 로 'put' 하는 경우 = 치즈를 수정합니다.
    def put(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('cheese_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            cheese_id = kwargs.get('cheese_id')
            cheese_object = Cheese.objects.get(id=cheese_id)
            if cheese_object.existence:
                update_cheese_serializer = CheeseSerializer(cheese_object, data=request.data)
                # 유효한 요청을 확인
                if update_cheese_serializer.is_valid():
                    update_cheese_serializer.save()
                    return Response(update_cheese_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'cheese/cheese_id' 로 'delete' 하는 경우 = 치즈를 삭제합니다.
    def delete(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('cheese_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            cheese_id = kwargs.get('cheese_id')
            cheese_object = Cheese.objects.get(id=cheese_id)
            if cheese_object.existence:
                cheese_name = cheese_object.name
                cheese_object.existence = False
                cheese_object.save()
                # 삭제한 치즈의 이름을 알림
                return Response(f"{cheese_name} has been deleted", status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)

class SauceView(APIView):
    # 'sauce/' 로 'post' 하는 경우 = 소스를 추가합니다.
    def post(self, request):
        sauce_serializer = SauceSerializer(data=request.data) # Request의 data를 SauceSerializer로 변환
        # 유효한 요청을 확인
        if sauce_serializer.is_valid():
            sauce_serializer.save() # SauceSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(sauce_serializer.data, status=status.HTTP_201_CREATED) # client에게 JSON response 전달
        else:
            return Response(sauce_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 'sauce/' 로 'get' 하는 경우 = 소스 목록을 조회합니다.
    # 'sauce/sauce_id' 로 'get' 하는 경우 = 소스를 조회합니다.
    def get(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('sauce_id') is None:
            sauce_queryset = Sauce.objects.all() # 모든 sauce의 정보를 불러온다.
            sauce_queryset = sauce_queryset.filter(Q(existence=True)).distinct()
            sauce_queryset_serializer = SauceSerializer(sauce_queryset, many=True)
            return Response(sauce_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            sauce_id = kwargs.get('sauce_id')
            sauce_queryset = Sauce.objects.get(id=sauce_id)
            if sauce_queryset.existence:
                sauce_serializer = SauceSerializer(sauce_queryset) # id에 해당하는 sauce의 정보를 불러온다.
                return Response(sauce_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'sauce/sauce_id' 로 'put' 하는 경우 = 소스를 수정합니다.
    def put(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('sauce_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            sauce_id = kwargs.get('sauce_id')
            sauce_object = Sauce.objects.get(id=sauce_id)
            if sauce_object.existence:
                update_sauce_serializer = SauceSerializer(sauce_object, data=request.data)
                # 유효한 요청을 확인
                if update_sauce_serializer.is_valid():
                    update_sauce_serializer.save()
                    return Response(update_sauce_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response('Invalid Request', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
    # 'sauce/sauce_id' 로 'delete' 하는 경우 = 소스를 삭제합니다.
    def delete(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('sauce_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            sauce_id = kwargs.get('sauce_id')
            sauce_object = Sauce.objects.get(id=sauce_id)
            if sauce_object.existence:
                sauce_name = sauce_object.name
                sauce_object.existence = False
                sauce_object.save()
                # 삭제한 소스의 이름을 알림
                return Response(f"{sauce_name} has been deleted", status=status.HTTP_200_OK)
            else:
                return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)

# input = list[QueryObject, QueryObject, ...]
# ouput = List[None] or list[str, str, ...]
def check_ingredients(ingredient_list):
    # 재료 중 0개인 재료가 있으면 이름을 반환
    lacking_ingredients = []
    for ingredient in ingredient_list:
        if not ingredient.stock:
            lacking_ingredients.append(ingredient.name)
    return lacking_ingredients

# input = queryset(모든 샌드위치), str(keyword), int(id)
# output = queryset(검색 결과 샌드위치)
def search_kw_kn(queryset, kw, kn):
    if kw == 'bread':
        queryset = queryset.filter(Q(bread__id__icontains=kn)).distinct()
    elif kw == 'topping':
        queryset = queryset.filter(Q(topping__id__icontains=kn)).distinct()
    elif kw == 'cheese':
        queryset = queryset.filter(Q(cheese__id__icontains=kn)).distinct()
    else:
        queryset = queryset.filter(Q(sauce__id__icontains=kn)).distinct()
    return queryset

class SandwichView(APIView):
    # 'sandwich/' 로 'post' 하는 경우 = 샌드위치를 만듭니다.
    def post(self, request):
        ingredients=request.data
        sandwich_serializer = SandwichSerializer(data=ingredients) # Request의 data를 SandwichSerializer로 변환
        # 재료 오브젝트 설정
        bread_object = Bread.objects.get(id=ingredients['bread'])
        topping_object = Topping.objects.get(id=ingredients['topping'])
        cheese_object = Cheese.objects.get(id=ingredients['cheese'])
        sauce_object = Sauce.objects.get(id=ingredients['sauce'])
        if bread_object.existence and topping_object.existence and cheese_object.existence and sauce_object.existence:
            ingredient_objects = [
                bread_object, topping_object, 
                cheese_object, sauce_object
                ]
        else:
            return Response('Deleted Data', status=status.HTTP_400_BAD_REQUEST)
        # 별도의 함수를 통해 없는 재료가 있는 지 확인
        check_stock = check_ingredients(ingredient_objects)
        # 없는 재료가 있다면 알림
        if check_stock:
            return Response(f"No more {check_stock}", status=status.HTTP_400_BAD_REQUEST)
        # 유효한 요청을 확인
        elif sandwich_serializer.is_valid():
            sandwich_serializer.save() # SandwichSerializer의 유효성 검사를 한 뒤 DB에 저장
            # 재료의 재고 -1
            for ingredient in ingredient_objects:
                ingredient.stock -= 1
                ingredient.save()
            return Response(sandwich_serializer.data, status=status.HTTP_201_CREATED) # client에게 JSON response 전달
        else:
            return Response(sandwich_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 'sandwich/' 로 'get' 하는 경우 = 샌드위치 목록을 조회합니다.
    # 'sandwich/sandwich_id' 로 'get' 하는 경우 = 샌드위치를 조회합니다.
    def get(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('sandwich_id') is None:
            sandwich_queryset = Sandwich.objects.all() # 모든 sandwich의 정보를 불러온다.
            sandwich_queryset = sandwich_queryset.filter(Q(existence=True)).distinct()
            # 검색 조건이 요청에 있는 지 확인
            kw_list = ('bread', 'topping', 'cheese', 'sauce', 'price')
            if kwargs.get('sandwich_kw') in kw_list and kwargs.get('kw_kn'):
                sandwich_queryset = search_kw_kn(sandwich_queryset, kwargs.get('sandwich_kw'), kwargs.get('kw_kn'))
            # 페이지 요청이 있는 지 확인
            # paginator 활용 pagination
            if kwargs.get('page'):
                paginator = Paginator(sandwich_queryset, 10)
                page = kwargs.get('page')
                sandwich_queryset_serializer = SandwichSerializer(paginator.get_page(page), many=True)
            else:
                sandwich_queryset_serializer = SandwichSerializer(sandwich_queryset, many=True)
            return Response(sandwich_queryset_serializer.data, status=status.HTTP_200_OK)
        # id가 요청에 있는 경우
        else:
            sandwich_id = kwargs.get('sandwich_id') # id에 해당하는 sandwich의 정보를 불러온다.
            sandwich = Sandwich.objects.get(id=sandwich_id)
            if not sandwich.existence:
                sandwich_id = f'{sandwich_id}-Deleted Sandwich'
            # 상세 정보 가져오기
            bread_object = Bread.objects.get(id=sandwich.bread_id)
            topping_object = Topping.objects.get(id=sandwich.topping_id)
            cheese_object = Cheese.objects.get(id=sandwich.cheese_id)
            sauce_object = Sauce.objects.get(id=sandwich.sauce_id)
            # 빵, 토핑, 치즈, 소스의 이름, 재고, 가격 정보 제공
            return Response(
                    {'id':sandwich_id,
                    'price':sum(
                        [bread_object.price, bread_object.price, 
                        cheese_object.price, sauce_object.price]
                        ), 
                    'ingredients':{
                            'bread':{'name':bread_object.name, 'stock':bread_object.stock, 'price':bread_object.price},
                            'topping':{'name':topping_object.name, 'stock':topping_object.stock, 'price':bread_object.price}, 
                            'cheese':{'name':cheese_object.name, 'stock':cheese_object.stock, 'price':cheese_object.price}, 
                            'sauce':{'name':sauce_object.name, 'stock':sauce_object.stock, 'price':sauce_object.price}
                        }
                    }, 
                    status=status.HTTP_200_OK)
    # 'sandwich/sandwich_id' 로 'delete' 하는 경우 = 샌드위치를 삭제합니다.
    def delete(self, request, **kwargs):
        # id가 요청에 있는 지 확인
        if kwargs.get('sandwich_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        # id가 요청에 있는 경우
        else:
            sandwich_id = kwargs.get('sandwich_id')
            sandwich_object = Sandwich.objects.get(id=sandwich_id)
            # 상세 정보 가져오기
            bread_object = Bread.objects.get(id=sandwich_object.bread_id)
            topping_object = Topping.objects.get(id=sandwich_object.topping_id)
            cheese_object = Cheese.objects.get(id=sandwich_object.cheese_id)
            sauce_object = Sauce.objects.get(id=sandwich_object.sauce_id)
            ingredient_objects = [
                bread_object, topping_object, 
                cheese_object, sauce_object
                ]
            # 재료 목록과 총 가격
            total_ingredients = []
            total_price = 0
            for ingredient in ingredient_objects:
                total_ingredients.append(ingredient.name)
                total_price += ingredient.price
                # 재료 되돌리기
                ingredient.stock += 1
                ingredient.save()
            sandwich_object.existence = False
            sandwich_object.save()
            # 삭제한 샌드위치의 재료 목록과 총 가격
            return Response({sandwich_id:{'total ingredients':total_ingredients, 'total price':total_price}}, status=status.HTTP_200_OK)