# Setup

## :a: LMS Assignment ID = 18

```
https://${LMS_URL}/mod/assign/view.php?id=18
```

```json
{
  "id": 18,        // Assignment ID
  "cmid": 22,      // Rubric Definition CMID
  "name": "5.OOP"  // Assignment name
}
```

## :b: Rubric Definition for

- [ ] cmids[0]=22

- [ ] Retrieve all rubric definitions from LMS


```bash
curl -X POST "https://${LMS_URL}/webservice/rest/server.php" \
-d "wstoken=${API_SYNC_TOKEN}" \
-d "wsfunction=core_grading_get_definitions" \
-d "moodlewsrestformat=json" \
-d "cmids[0]=22" \
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
      "cmid": 22,
      "contextid": 475,
      "component": "mod_assign",
      "areaname": "submissions",
      "activemethod": "rubric",
      "definitions": [
        {
          "id": 17,
          "method": "rubric",
          "name": "🅰️ Présence",
          "description": "",
          "descriptionformat": 1,
          "status": 20,
          "copiedfromid": null,
          "timecreated": 1776949046,
          "usercreated": 3,
          "timemodified": 1776949698,
          "usermodified": 3,
          "timecopied": 0,
          "rubric": {
            "rubric_criteria": [
              {
                "id": 82,
                "sortorder": 1,
                "description": "README.md",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 188,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 189,
                    "score": 1,
                    "definition": "🥈",
                    "definitionformat": 1
                  },
                  {
                    "id": 190,
                    "score": 2,
                    "definition": "🥇",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 83,
                "sortorder": 2,
                "description": "images",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 191,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 192,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 84,
                "sortorder": 3,
                "description": "🚀 main.py",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 193,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 194,
                    "score": 1,
                    "definition": "‼️ ou 💥",
                    "definitionformat": 1
                  },
                  {
                    "id": 203,
                    "score": 2,
                    "definition": "🚀",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 85,
                "sortorder": 4,
                "description": "🧾 RAPPORT",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 195,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 196,
                    "score": 1,
                    "definition": "🧾",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 86,
                "sortorder": 5,
                "description": "✍️ Sgn",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 197,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 198,
                    "score": 1,
                    "definition": "✍️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 87,
                "sortorder": 6,
                "description": "🖼️ Figures",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 199,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 200,
                    "score": 1,
                    "definition": "0️⃣",
                    "definitionformat": 1
                  },
                  {
                    "id": 204,
                    "score": 2,
                    "definition": "*️⃣",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 88,
                "sortorder": 7,
                "description": "requirements.txt",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 201,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 202,
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
