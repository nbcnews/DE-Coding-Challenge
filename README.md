# NBC DE Coding Challenge
Data Engineering Coding Challenge

## Instructions
You will be working on following coding challenges
    
    Challenge-1 : Refactor existing code following the best practices and coding conventions

    Challenge-2 : Read bitcoin api and structure the api in a given schema format

### Challenge-1:

### [TODO](https://github.com/nbcnews/DE-Coding-Challenge/blob/master/Challenge-1/src/csv_parser.py)
- [ ] Refactor **csv_parser.py** 
- [ ] Justify your changes


### Challenge-2:

**Note:** Feel free to change method signatures and constant/variable values.

### [TODO A](https://github.com/nbcnews/DE-Coding-Challenge/blob/master/Challenge-2/processor/process_content.py#L11)
- [ ] Inspect bitcoin API Manually https://api.coinranking.com/v1/public/coin/1/history/30d
- [ ] Read bitcoin API in the code and return data in JSON format (This API Contains last 30 days bitcoin data)

### [TODO B](https://github.com/nbcnews/DE-Coding-Challenge/blob/master/Challenge-2/processor/process_content.py#L30)
- [ ] Transform API data into following JSON schema

      ` Output schema:
        {
            "date": "{date}",
            "price": "{value}",
            "direction": "{up/down/same}",
            "change": "{amount}",
            "dayOfWeek": "{name}”,
            "highSinceStart": "{true/false}”,
            "lowSinceStart": "{true/false}”
        }`
  - one entry per day at "00:00:00" hours
 
  - results ordered by oldest date first.
 
  - "date" in format "2019-03-17T00:00:00"
 
  - "price" in 2 decimal dollars
 
  - "direction" is direction of price change since previous day in the list, first day can be "na" ({up/down/same})
 
  - "change" is the price difference between current and previous day. "na" for first
 
  - "dayOfWeek" is name of the day (Saturday, Tuesday, etc)
 
  - "highSinceStart" true/false if highest since list start. "na" for first

- [ ] Return Transformed JSON.

### [TODO C](https://github.com/nbcnews/DE-Coding-Challenge/blob/master/Challenge-2/processor/process_content.py#L41)
- [ ] Call required methods in the handler code
- [ ] Check output matches and returns the expected value 

**Note:** Please feel free to use Jupyter notebook for both challenges, repository contains a notebook file in case needed.