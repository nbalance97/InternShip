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

## Django API 사용
- Ajax 연동을 통해 데이터 추가 
---
```python
    path('api/', IC_list, name="api-company-list"),
    path('api/<int:pk>/', IC_detail, name="api-company-detail"),
```

## Template
1. Bootstrap Template 사용
    - https://bootswatch.com/journal/
2. widget_tweaks 사용하여 Form 클래스 변경
