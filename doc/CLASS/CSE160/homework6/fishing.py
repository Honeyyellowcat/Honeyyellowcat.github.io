import csv  # noqa: F401
import os  # noqa: F401
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as poly  # noqa: F401


def min_year(fieldnames):
    years = [int(name) for name in fieldnames[3:] if name.isdigit()]
    return min(years)

def max_year(fieldnames):
    years = [int(name) for name in fieldnames[3:] if name.isdigit()]
    return max(years)

def parse_data(filename):
    data = {"min_year": None, "max_year": None, "farmed": {}, "wild caught": {}, "consumption": {}, "population": {}}
    
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        data["min_year"] = min_year(fieldnames)
        data["max_year"] = max_year(fieldnames)

        for row in reader:
            country_code = row['country code']
            measure = row['measure']
            if country_code not in data[measure]:
                data[measure][country_code] = {}
            
            for year in fieldnames[3:]:
                value = row[year]
                if value == '':
                    data[measure][country_code][int(year)] = None
                else:
                    if measure == 'consumption':
                        data[measure][country_code][int(year)] = float(value)
                    else:
                        data[measure][country_code][int(year)] = int(value)
    
    return data


def get_actual_production(data, country_code, year):
    """
    Combines the "farmed" and "wild caught" fields from `data` for the given
    country and year into a single value. Returns an integer.
    """
    farmed = data["farmed"].get(country_code, {}).get(year)
    wild_caught = data["wild caught"].get(country_code, {}).get(year)

    if farmed is None and wild_caught is None:
        return None
    elif farmed is None:
        return wild_caught
    elif wild_caught is None:
        return farmed
    else:
        return farmed + wild_caught


def get_production_need(data, country_code, year):
    """
    Based on the population and consumption values in `data`, calculates the
    amount of production that is needed to meet consumption needs for a given
    country in the given year. Returns a float.
    """
    population = data["population"].get(country_code, {}).get(year)
    consumption = data["consumption"].get(country_code, {}).get(year)

    if population is None or consumption is None:
        return None
    else:
        return population * consumption / 1000


def plot_production_vs_consumption(data, country_code):
    """
    Given a country code and the data dictionary, plots a line graph of the
    actual production against the calculated needed production over time.
    """
    years = range(data["min_year"], data["max_year"] + 1)
    actual_production = []
    production_need = []

    for year in years:
        actual = get_actual_production(data, country_code, year)
        need = get_production_need(data, country_code, year)

        if actual is not None and need is not None:
            actual_production.append(actual)
            production_need.append(need)

    plt.plot(years[:len(actual_production)], actual_production, label="Actual Production")
    plt.plot(years[:len(production_need)], production_need, label="Production Need")
    plt.xlabel("Year")
    plt.ylabel("Production (metric tons)")
    plt.title(f"Production vs. Consumption for {country_code}")
    plt.legend()
    plt.grid(True)
    plt.show()


def predict_need(data, country_code, predict_years):
    """
    Returns a dictionary that represents a best-fit prediction line for the given
    `country_code` over the next `predict_years` years.

    You will be asked to write this function in Problem 4a.
    """
    observed_years = []
    observed_values = []

    # Collect observed data
    for year in range(data["min_year"], data["max_year"] + 1):
        production_need = get_production_need(data, country_code, year)
        if production_need is not None:
            observed_years.append(year)
            observed_values.append(production_need)

    # Calculate best-fit line
    b, m = poly.polyfit(observed_years, observed_values, 1)

    # Generate values
    prediction_years = list(range(data["max_year"] + 1, data["max_year"] + predict_years + 1))
    prediction_values = [m * year + b for year in prediction_years]

    return {"years": prediction_years, "values": prediction_values}


def plot_linear_prediction(data, country_code):
    '''
    A function that takes the output of `parse_data("small.csv")` as its first
    parameter and a country code (e.g., "USA") as its second parameter. It
    then calls the `calculate_prediction` function with the production need
    data (from get_production_need) for the given country code, and then
    plots the best-fit line and prediction.

    NOTE: This is a complete function, you do not need to modify it. However,
    it relies on parse_data, get_production_need, and calculate_prediction to
    be implemented according to the assignment spec.
    '''
    real_min_year = data['min_year']
    real_max_year = data['max_year']
    observed_need_years = list(range(real_min_year, real_max_year + 1))
    observed_need_values = [get_production_need(data, country_code, year)
                            for year in observed_need_years]
    plt.plot(observed_need_years, observed_need_values, label='data', linestyle='', marker='s')

    prediction = predict_need(data, country_code, 50)
    plt.plot(prediction['years'], prediction['values'],
             linestyle='--', label='best-fit prediction')

    plt.title('Predicted Production Need For ' + country_code)
    plt.xlabel('Year')
    plt.ylabel('Metric Tonnes')
    plt.legend()
    plt.savefig(os.path.dirname(__file__) + "/" + country_code + "_need_prediction.png")

# Call data
data = parse_data("small.csv")
plot_linear_prediction(data, "USA")

def total_production_need(data, years_to_predict):
    """
    Calculates the total production need for the entire world for the specified
    number of years in the future.

    Args:
    - data (dict): Parsed data from parse_data function.
    - years_to_predict (int): Number of years in the future to predict.

    Returns:
    - float: Total production need in metric tonnes.
    """
    total_need = 0

    # Predict production need for each country
    for country_code in data["consumption"]:
        prediction = predict_need(data, country_code, years_to_predict)
        last_value = prediction["values"][-1]
        total_need += last_value

    return total_need
pass


def min_year(fields):
    '''
    A helper function that, given a list of values, returns
    the minimum integer.

    You do not have to modify or even use this function, but it is here
    if you want to use it. It is suggested to use it in `parse_data`.
    '''
    return min([int(field) for field in fields
                if type(field) is int or field.isnumeric()])


def max_year(fields):
    '''
    A helper function that, given a list of values, returns 
    the maximum integer.

    You do not have to modify or even use this function, but it is here
    if you want to use it. It is suggested to use it in `parse_data`.
    '''
    return max([int(field) for field in fields
                if type(field) is int or field.isnumeric()])


if __name__ == "__main__":
    # Parse data from large.csv
    data = parse_data("large.csv")
    
    # Calculate and print total production need for 50 years in the future
    total_need_50_years = total_production_need(data, 50)
    print(f"Metric tonnes of seafood needed to be produced in 50 years: {total_need_50_years:,.3f}")
