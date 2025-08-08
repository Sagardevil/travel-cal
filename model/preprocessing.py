import pandas as pd

def preprocess_input(form_data):
    """Convert form data to DataFrame with correct structure"""
    # Create DataFrame with all expected columns
    expected_columns = [
        'Age', 'DurationOfPitch', 'Gender', 'NumberOfTrips', 'OwnCar',
        'NumberOfPersonVisiting', 'MaritalStatus', 'PreferredPropertyStar',
        'NumberOfFollowups', 'CityTier', 'TypeofContact', 'PitchSatisfactionScore',
        'ProductPitched', 'ProdTaken', 'Designation', 'NumberOfChildrenVisiting',
        'Passport', 'City', 'Occupation'
    ]
    
    # Create DataFrame with all columns initialized to None
    features = pd.DataFrame(columns=expected_columns)
    
    # Fill in provided values
    for col in expected_columns:
        if col in form_data:
            features[col] = [form_data[col]]
    
    # Convert numeric fields
    numeric_fields = [
        'Age', 'DurationOfPitch', 'NumberOfTrips', 'NumberOfPersonVisiting',
        'PreferredPropertyStar', 'NumberOfFollowups', 'CityTier',
        'PitchSatisfactionScore', 'NumberOfChildrenVisiting'
    ]
    for field in numeric_fields:
        if field in features.columns:
            features[field] = pd.to_numeric(features[field], errors='coerce')
    
    return features