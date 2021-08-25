---
# InternShip Project
---

Internship Project
- Django의 Form, Model, View, url 매핑 등을 활용하여 간단한 사이트 구현
- API 구현 
- Ajax 사용해보는 경험

---
# model
---

1. InterestCompany

| 필드명 | 타입 |
| ------ | --- |
| 사용자 | User |
| 회사명 | CharField |
| 인턴십 제목 | CharField |
| 만기 기한 | DateTimeField |

2. User
- Django의 User 모델 그대로 사용

---
## Django의 제네릭 뷰 활용
---

1. InterestCompanyListView -> 관심 회사 전체 조회 / 페이지네이션 적용
2. InterestCompanyCreateView -> 관심 회사 데이터 생성
3. InterestCompanyDeleteView -> 관심 회사 데이터 제거
4. InterestCompanyUpdateView -> 관심 회사 데이터 변경
---
## Django API 사용
- Ajax 연동을 통해 데이터 추가 
---
0. Serializer 설정
    - Django Model과 JavaScript 사이에서 서로 사용할 수 있도록 쉽게 변환하기 위해 사용
    - 직접 해본 결과 request.data에는 QueryDict 타입의 딕셔너리와 비슷한 데이터가 들어옴.
    - 해당 데이터로 Serializer을 생성하면, 자동으로 deserialize 되는듯.
    - 직접 해본 결과
        -  응답할 떄 : response(Serializer.data)
        -  가져올 때 : Serializer(data=request.data)
``` python
from rest_framework import serializers
from .models import InterestCompany


class InterestCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestCompany
        fields = "__all__"
```

1. ViewSet 설정 (ModelView 설정)
    - 기본적으로는 ModelViewSet에서 list(), retrieve(), create() 등등을 제공함.
    - 동작 원리를 파악하고자 직접 함수 지정해봄
    - method -> post일때, 데이터 생성하도록 지정
    - action에서 detail의 경우에는 pk를 사용할 때 True, 사용하지 않으면 False
    - pk를 사용하는 경우에는 함수의 매개변수 내에 pk=None 추가해야 하는듯.
```python
class InterestCompanyViewSet(viewsets.ModelViewSet):
    queryset = InterestCompany.objects.all()
    serializer_class = InterestCompanySerializer

    @action(detail=False, methods=['post'])
    def create_interestcompany(self, request):
        serializer = InterestCompanySerializer(data=request.data)
        if serializer.is_valid():
            InterestCompany.objects.create(
                user=serializer.validated_data['user'],
                company_name=serializer.validated_data['company_name'],
                intern_title=serializer.validated_data['intern_title'],
                duration=serializer.validated_data['duration']
            ) # serializer.create(serializer.validated_data)로 대체 가능
            return Response({'status': 'create interestcompany'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
```
---
2. URL 설정
    - 나머지 method는 기본 제공 함수 사용
    - "post" 에서는 create_interestcompany 함수 호출하도록 지정
```python
    IC_list = InterestCompanyViewSet.as_view({
        'post': 'create_interestcompany',
        'get': 'list'
    })

    IC_detail = InterestCompanyViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })

    path('api/', IC_list, name="api-company-list"),
    path('api/<int:pk>/', IC_detail, name="api-company-detail"),
```

---
3. Script 설정
    - csrftoken을 같이 보내주어야 에러가 나타나지 않음!!
    - csrftoken을 보내주는 방법
    ``` javascript
    const csrftoken = getCookie('csrftoken');

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    ```
    
- Ajax 설정
``` javascript
        $.ajax({
            type: "POST",
            url: "{% url 'api-company-list' %}",
            data: {
                "user" : userId,
                "company_name" : name,
                "intern_title" : title,
                "duration" : input_duration,
            },
            dataType: "json",
            beforeSend: function(request) {
                request.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(response) {
                window.location.reload()
            },
            error: function(request, status, error) {
                console.log("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+error);
            }
        });
```


## Template
1. Bootstrap Template 사용
    - https://bootswatch.com/journal/
2. widget_tweaks 사용하여 Form 클래스 변경

# 화면

## 메인 화면

![image](https://user-images.githubusercontent.com/76891875/129441862-803fa4c4-429d-4d81-ae38-208b4a5d2995.png)

![image](https://user-images.githubusercontent.com/76891875/129441875-c6aa3d7e-e7e8-4054-9697-87bb7f09914e.png)



## 로그인

![image](https://user-images.githubusercontent.com/76891875/129441893-286c9063-f250-4f93-a7ad-4918d17ea9e8.png)

## 회원가입

![image](https://user-images.githubusercontent.com/76891875/129441901-2ada13a7-6c41-420c-957b-b6debe1dae75.png)


## 참고

https://www.django-rest-framework.org/api-guide/viewsets/#api-reference
