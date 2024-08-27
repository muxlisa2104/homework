talaba = {
  "student" : [
    {
      "id": "01",
      "name": "Tom",
      "lastname": "Price",
      "year": 4,
      "faculty": "Engineering"
    },
    {
      "id": "02",
      "name": "Nick",
      "lastname": "Thameson",
      "year": 3,
      "faculty": "Computer Science"
    },
    {
      "id": "03",
      "name": "John",
      "lastname": "Doe",
      "year": 2,
      "faculty": "ICT"
    }
  ]
}
for s in talaba['student']:
  print(
    f"Ismi: {s['name']} {s['lastname']}. "
    f"{s['year']}-kurs, {s['faculty']} fakultet talabasi")
