# Setup

## :a: Class - INF1093-201-26H-05 - Programmation 2

```
https://${LMS_URL}/course/view.php?id=5
```

## :b: Assignments for:

- [ ] courseids[0]=5

```json
{
  "id": 4,        // Assignment ID
  "cmid": 6,      // Rubric Definition CMID
  "name": "2.IO"  // Assignment name
}
```


- [ ] Retrieve all assignments from LMS


```bash
curl -X POST "https://${LMS_URL}/webservice/rest/server.php" \
-d "wstoken=${API_SYNC_TOKEN}" \
-d "wsfunction=mod_assign_get_assignments" \
-d "moodlewsrestformat=json" \
-d "courseids[0]=5" | jq '.courses[].assignments[] | {id, cmid, name}'
```
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1704    0  1587  100   117   2463    181 --:--:-- --:--:-- --:--:--  2645
```
<details><summary>📑</summary>

```json
{
  "id": 4,
  "cmid": 8,
  "name": "2.IO"
}
{
  "id": 6,
  "cmid": 10,
  "name": "3.Tris"
}
{
  "id": 17,
  "cmid": 21,
  "name": "4.Hashing"
}
{
  "id": 18,
  "cmid": 22,
  "name": "5.OOP"
}
{
  "id": 19,
  "cmid": 23,
  "name": "8.Dijkstra"
}
```

</details>


