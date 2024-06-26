### Algerian Forest Fire

### Software and Tools Required

1. [Github Account](https://github.com/)
2. [VS Code IDE](https://code.visualstudio.com)

Create a new environment

``` 
python -m venv env
.\env\Scripts\activate
```

Install required packages

```
pip install -r requirements.txt
```

# Weather and FWI System Report

## Weather System Report
This report analyzes the correlation between weather conditions and forest fire occurrences.

### Key Findings:
- **Temperature**: The highest fire counts occurred between **30-37 degrees Celsius**.
- **Rain**: Highest fire counts happened when there was no rain to very little rain (0.0 to 0.3).
- **Wind Speed**: Highest fire counts occurred when the wind speed was between **13 to 19 km/hr**.
- **Relative Humidity (RH)**: Highest fire counts happened when RH was between **50 to 80%**.

## FWI System Components Report
The FWI (Canadian Forest Fire Weather Index) system components analysis provides insights into fire risk based on specific indices.

### Components:
- **Fine Fuel Moisture Code (FFMC)**: Ranges between 28.6 to 92.5. Values above 75 indicate a higher chance of forest fires.
- **Duff Moisture Code (DMC)**: Ranges between 1.1 to 65.9. Values above 10-30 DMC indicate very high evidence of forest fires.
- **Drought Code (DC)**: Ranges between 7 to 220.4. Values above 25 DC indicate higher chances of forest fires.
- **Initial Spread Index (ISI)**: Ranges between 0 to 18. Values above 3 ISI indicate higher chances of forest fires.
- **Buildup Index (BUI)**: Ranges between 1.1 to 68. Values above 10 BUI indicate higher chances of forest fires.
- **Fire Weather Index (FWI)**: Ranges between 1 to 31.1. Values above 3-25 FWI indicate higher chances of forest fires.

This report helps in understanding the relationship between weather conditions and the risk of forest fires based on the FWI indices.

