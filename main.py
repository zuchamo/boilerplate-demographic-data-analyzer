# main.py

from demographic_data_analyzer import calculate_demographic_data

def test_calculate_demographic_data():
    results = calculate_demographic_data(print_data=False)

    # Assert checks (these are illustrative — update expected values based on your actual dataset)
    assert isinstance(results['race_count'], pd.Series), "Race count should be a pandas Series"
    assert isinstance(results['average_age_men'], float), "Average age should be a float"
    assert 0 <= results['percentage_bachelors'] <= 100, "Percentage should be within 0-100 range"
    assert results['highest_earning_country_percentage'] > 0, "Should be greater than 0"

    print("✅ All test checks passed!")

if __name__ == "__main__":
    test_calculate_demographic_data()
