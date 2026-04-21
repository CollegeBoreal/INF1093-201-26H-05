```bash
curl -X POST "https://${LMS_URL}/webservice/rest/server.php" \
-d "wstoken=${API_SYNC_TOKEN}" \
-d "wsfunction=core_grading_get_definitions" \
-d "moodlewsrestformat=json" \
-d "cmids[0]=8" \
-d "areaname=submissions" | jq .
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2397    0  2261  100   136   3849    231 --:--:-- --:--:-- --:--:--  4076
```
```json
{
  "areas": [
    {
      "cmid": 8,
      "contextid": 443,
      "component": "mod_assign",
      "areaname": "submissions",
      "activemethod": "rubric",
      "definitions": [
        {
          "id": 3,
          "method": "rubric",
          "name": "Participation",
          "description": "2️⃣ I/O (Input/Output)",
          "descriptionformat": 1,
          "status": 20,
          "copiedfromid": null,
          "timecreated": 1776695382,
          "usercreated": 3,
          "timemodified": 1776745403,
          "usermodified": 3,
          "timecopied": 0,
          "rubric": {
            "rubric_criteria": [
              {
                "id": 5,
                "sortorder": 1,
                "description": "README.md",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 13,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 14,
                    "score": 1,
                    "definition": "🥈",
                    "definitionformat": 1
                  },
                  {
                    "id": 15,
                    "score": 2,
                    "definition": "🥇",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 6,
                "sortorder": 2,
                "description": "images",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 16,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 17,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 7,
                "sortorder": 3,
                "description": "🚀 IO.py",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 18,
                    "score": 0,
                    "definition": "❔",
                    "definitionformat": 1
                  },
                  {
                    "id": 19,
                    "score": 1,
                    "definition": "🚀",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 8,
                "sortorder": 4,
                "description": "🧾 RAPPORT",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 20,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 21,
                    "score": 1,
                    "definition": "🧾",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 9,
                "sortorder": 5,
                "description": "✍️ Sgn",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 22,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 23,
                    "score": 1,
                    "definition": "✍️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 10,
                "sortorder": 6,
                "description": "🖼️ Figures",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 24,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 25,
                    "score": 1,
                    "definition": "1️⃣",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 11,
                "sortorder": 7,
                "description": "etudiants.txt",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 26,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 27,
                    "score": 1,
                    "definition": "✔️",
                    "definitionformat": 1
                  }
                ]
              },
              {
                "id": 12,
                "sortorder": 8,
                "description": "resultats.txt",
                "descriptionformat": 1,
                "levels": [
                  {
                    "id": 28,
                    "score": 0,
                    "definition": "❌",
                    "definitionformat": 1
                  },
                  {
                    "id": 29,
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
