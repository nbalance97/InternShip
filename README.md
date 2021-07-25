# InternShip
Internship Project
- Django의 Form, Model, View, url 매핑 등을 활용하여 간단한 사이트 구현
- API 구현 
- Ajax 사용해보는 경험

# model
## 테이블 구조
| 필드명 | 타입 |
| ------ | --- |
| 회사명 | CharField |
| 인턴십 제목 | CharField |
| 만기 기한 | DateTimeField |

## models.py 작성
``` python
  class InterestCompany(models.Model):
    company_name = models.CharField(max_length=100)
    intern_title = models.CharField(max_length=100)
    duration = models.DateTimeField()
```

# url 매핑
## Project App
- Interest App로 url 넘겨줌
``` python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Interest.urls'))
]
```

### Interest App
- CRUD 관련된 뷰를 사용
- company_id는 해당 company의 기본키
- api, api/<pk> url 설정

``` python
urlpatterns = [
    path('interest/', views.InterestCompanyListView.as_view(), name='company-list'),
    path('interest/create', views.InterestCompanyCreateView.as_view(), name='company-create'),
    path('interest/<int:company_id>/delete', views.InterestCompanyDeleteView.as_view(), name='company-delete'),
    path('interest/<int:company_id>/modify', views.InterestCompanyUpdateView.as_view(), name='company-modify'),
    path('interest/api/', IC_list, name="api-company-list"),
    path('interest/api/<int:pk>/', IC_detail, name="api-company-detail"),
]
```

# View
## Django의 제네릭 뷰 활용
1. InterestCompanyListView -> 관심 회사 전체 조회 / 페이지네이션 적용
2. InterestCompanyCreateView -> 관심 회사 데이터 생성
3. InterestCompanyDeleteView -> 관심 회사 데이터 제거
4. InterestCompanyUpdateView -> 관심 회사 데이터 변경

# Process.py
### 사이트 파싱 -> 데이터를 리스트 반환하여 뷰로 전달
### 실제로 Django에서 나의 데이터가 아닌 실제 데이터를 활용해보고 싶어 파싱한 데이터 로드하는 기능 추가 
