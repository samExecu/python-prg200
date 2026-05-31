#dummy data
customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "full"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]

bs_months = [
    "Baisakh","Jestha","Ashadh","Shrawan","Bhadra","Ashwin",
    "Kartik","Mangsir","Poush","Magh","Falgun","Chaitra"
]

def convert_date(date_str, from_cal, to_cal):
  # Splitting the date string into year, month, day
  year, month, day = map(int, date_str.split("-"))

  #if both calendars are same, return the same value
  if from_cal == to_cal:
    return date_str

  #AD to BS, add 56 years
  if from_cal == "AD" and to_cal == "BS":
    year += 56

  #BS to AD, subtract 56 years
  elif from_cal == "BS" and to_cal == "AD":
    year -= 56

#return the converted date in YYYY-MM-DD format
  return f"{year:04d}-{month:02d}-{day:02d}"

#Going through each of the customer record
for customer in customers:
  converted = convert_date(customer["date"], customer["cal"], customer["need"])

  #Formatting based on style
  if customer["style"] == "iso":
    #Just show YYYY-MM-DD format
    output_date = f"{converted} {customer['need']}"

  elif customer["style"] == "full":
    #Show with day and month name
    y, m, d = map(int, converted.split("-"))

    if customer["need"] == "BS":
      month_name = bs_months[m-1]
      output_date = f"{d}th {month_name}, {y} {customer['need']}"

    else:
      output_date = f"{converted} {customer['need']}"

  elif customer["style"] == "nepali":
    #Show Nepali month name format
    y, m, d = map(int, converted.split("-"))
    month_name = bs_months[m-1]
    output_date = f"{d} {month_name} {y} {customer['need']}"

  else:
    output_date = f"{converted} {customer['need']}"

#display according to the users need
print(f"{customer['name']} | Original: {customer['date']} {customer['cal']} | Converted: {output_date}")
