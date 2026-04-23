# Setup

## :a: LMS Assignment ID = 19

```
https://${LMS_URL}/mod/assign/view.php?id=19
```

```json
{
  "id": 19,             // Assignment ID
  "cmid": 23,           // Rubric Definition CMID
  "name": "8.Dijkstra"  // Assignment name
}
```

## :b: Rubric Definition for

- [ ] cmids[0]=23

- [ ] Retrieve all rubric definitions from LMS


```bash
curl -X POST "https://${LMS_URL}/webservice/rest/server.php" \
-d "wstoken=${API_SYNC_TOKEN}" \
-d "wsfunction=core_grading_get_definitions" \
-d "moodlewsrestformat=json" \
-d "cmids[0]=23" \
-d "areaname=submissions" | jq .
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2397    0  2261  100   136   3849    231 --:--:-- --:--:-- --:--:--  4076
```
<details><summary>📑</summary>

```json
{
  "areas": [
    {
      "cmid": 23,
      "contextid": 476,
      "component": "mod_assign",
      "areaname": "submissions",
      "activemethod": "rubric",
      "definitions": [
        {
          "id": 18,
          "method": "rubric",
          "name": "🅰️ Présence",
          "description": "",
          "descriptionformat": 1,
          "status": 20,
          "copiedfromid": null,
          "timecreated": 1776949795,
          "usercreated": 3,
          "timemodified": 1776950067,
          "usermodified": 3,
          "timecopied": 0,
          "rubric": {
            "rubric_criteria": [
              {
                "id": 89,
                "sortorder": 1,
                "description": "README.md",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 205,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 206,
                    "score": 1,
                    "definition": "🥈",
                    "definitionformat": 1
                  },
                  {
                    "id": 207,
                    "score": 2,
                    "definition": "🥇",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 90,
                "sortorder": 2,
                "description": "images",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 208,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 209,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 93,
                "sortorder": 3,
                "description": "Structure",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 215,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 216,
                    "score": 1,
                    "definition": "🏗️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 91,
                "sortorder": 4,
                "description": "check_results",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 210,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 211,
                    "score": 1,
                    "definition": "🏁",
                    "definitionformat": 1
                  },
                  {
                    "id": 212,
                    "score": 2,
                    "definition": "🚀",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 92,
                "sortorder": 5,
                "description": "RAPPORT.ipynb",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 213,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 214,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              }
            ]
          }
        }
      ]
    }
  ],
  "warnings": []
}
```

</details>
