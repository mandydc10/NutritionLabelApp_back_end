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
|  wholefoods/   |      GET       |    Returns all wholefoods     |      N/A        |            200           |                Must be logged in.              |
|  wholefoods/   |      POST       |    Create new wholefood object    |      Wholefood Object        |        201               |            Must be logged in. Must be admin.                  |
|  wholefoods/almonds/   |      GET       |    Returns wholefood with slug of "almonds"     |       N/A       |            200           |               Must be logged in.               |
|  wholefoods/feedback/   |      GET       |    Returns all wholefoods     |       N/A       |             200          |               Must be logged in.               |
|  wholefoods/feedback/   |       POST      |    Create a new wholefood feedback       |      WholefoodFeedback object        |          201             |              Must be logged in. Must be practitioner user.                |
|  wholefoods/feedback/1/   |      GET       |        Returns a wholefood feedback object with ID of "1".    |      N/A        |            200           |               Must be logged in. Must be feedback owner or admin.               |
|  micronutrients/   |      GET       |     Returns all micronutrients    |       N/A       |            200           |             Must be logged in.                 |
|  micronutrients/   |       POST      |    Create new micronutrient object      |       Micronutrient Object       |          201             |                  Must be logged in. Must be admin.            |
|  micronutrients/vitamin-a/   |      GET       |    Returns nutrient with slug of "vitamin-a"     |      N/A       |         200              |               Must be logged in.               |
|  micronutrients/feedback/   |      GET       |   Returns all micronutrient feedback      |       N/A       |       200                |             Must be logged in. Must be admin user.                 |
|  micronutrients/feedback/   |      POST       |    Create a new micronutrient feedback     |       MicronutrientFeedback object       |       201               |             Must be logged in. Must be practitioner or admin user.                  |
|  micronutrients/feedback/1/   |      GET       |    Returns a micronutrient feedback object with ID of "1".    |       N/A       |           200            |              Must be logged in. Must be feedback owner or admin.                |

### DB Schema
![]( {{ ./relative/path/to/schema/image.png }} )
