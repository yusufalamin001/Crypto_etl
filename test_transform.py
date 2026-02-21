from transform import transform

sample_data = [
    {
        "name": "Bitcoin",
        "current_price": 70000,
        "price_change_24h": 1000.50,
        "market_cap": 1381651251183,
        "total_volume": 20154184933
    },
    {
        "name": "Ethereum",
        "current_price": 3500,
        "price_change_24h": 50.25,
        "market_cap": 420000000000,
        "total_volume": 15000000000
    }
]

def test_transform_returns_correct_number_of_records():
    result = transform(sample_data)
    assert len(result) == 2

def test_transform_returns_correct_fields():
    result = transform(sample_data)
    first_record = result[0]
    assert "coin_name" in first_record
    assert "current_price" in first_record
    assert "price_change_24h" in first_record
    assert "recorded_at" in first_record

def test_transform_handles_empty_input():
    result = transform([])
    assert result == []

def test_transform_maps_fields_correctly():
    result = transform(sample_data)
    first_record = result[0]
    assert first_record["coin_name"] == "Bitcoin"
    assert first_record["current_price"] == 70000