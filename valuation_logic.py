class AgriculturalMachineryValuator:
    """
    Core logic for evaluating fair market value for agricultural machinery.
    Calculates prices based on technical data, usage history, and market trends.
    """
    
    def __init__(self):
        self.base_depreciation_rate = 0.15  # Annual depreciation

    def calculate_fair_value(self, original_price, age, usage_hours, condition_score):
        """
        Estimates the value of a machine.
        :param condition_score: 1.0 (Excellent) to 0.5 (Poor)
        """
        # Depreciation over time
        time_factor = (1 - self.base_depreciation_rate) ** age
        
        # Adjustment based on usage hours
        usage_factor = 1 - (usage_hours / 20000) # Assuming 20k hours max life
        
        # Final calculation
        estimated_value = original_price * time_factor * usage_factor * condition_score
        
        return max(estimated_value, original_price * 0.1) # Scrap value floor

# Example usage of the logic
if __name__ == "__main__":
    valuator = AgriculturalMachineryValuator()
    print("Initializing valuation engine...")
