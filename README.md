# NutritionLabelApp back-end
NutriQR

## Planning:
### Concept/Name
An app connected to physical food storage jar labels via QR code, that will provide nutritional information on wholefoods and nutrients

### Intended Audience/User Stories
Anyone can use this app if they have purchased the accompanying labels and created a personal account

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define endpoints }} 

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
|  admin/   |             |         |              |                       |          Must be logged in. Must be admin user.       |
|  users/   |             |         |              |                       |                              |
|  api-token-auth/   |             |         |              |                       |                              |
|  wholefoods/   |      GET       |         |              |                       |                              |
|  wholefoods/   |      POST       |         |              |                       |                              |
|  wholefoods/<slug:slug>/   |      GET       |         |              |                       |                              |
|  wholefoods/feedback/   |      GET       |         |              |                       |                              |
|  wholefoods/feedback/   |       POST      |         |              |                       |                              |
|  wholefoods/feedback/<int:pk>/   |      GET       |         |              |                       |                              |
|  micronutrients/   |      GET       |         |              |                       |                              |
|  micronutrients/   |       POST      |         |              |                       |                              |
|  micronutrients/vitamin-a/   |      GET       |    Returns nutrient with name of "Vitamin A"     |              |                       |                              |
|  micronutrients/feedback/   |      GET       |   Returns all micronutrient feedback      |              |                       |                              |
|  micronutrients/feedback/   |      POST       |    Creates new micronutrient feedback     |              |                       |                              |
|  micronutrients/feedback/<int:pk>/   |             |         |              |                       |                              |

### DB Schema
![]( {{ ./relative/path/to/schema/image.png }} )
