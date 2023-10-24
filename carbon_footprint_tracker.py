import streamlit as st
from carbon_footprint_tracker import Vehicle, EnergyConsumption, WasteProduction


class User:
    def __init__(self, vehicles, energy_consumption, waste_production):
        self.vehicles = vehicles
        self.energy_consumption = energy_consumption
        self.waste_production = waste_production

    def get_carbon_footprint(self):
        """Calculates the user's carbon footprint.

         Returns:
            The user's carbon footprint in kilograms of carbon dioxide.
         """

        # Calculate the carbon footprint from transportation.
        transportation_carbon_footprint = 0
        for vehicle in self.vehicles:
            transportation_carbon_footprint += vehicle.get_carbon_footprint()

        # Calculate the carbon footprint from energy consumption.
        energy_carbon_footprint = 0
        for energy_consumption in self.energy_consumption:
            energy_carbon_footprint += energy_consumption.get_carbon_footprint()

        # Calculate the carbon footprint from waste production.
        waste_carbon_footprint = 0
        for waste_production in self.waste_production:
            waste_carbon_footprint += waste_production.get_carbon_footprint()

        # Return the total carbon footprint.
        return transportation_carbon_footprint + energy_carbon_footprint + waste_carbon_footprint

@st.cache_data
def calculate_carbon_footprint(user):
    """Calculates the user's carbon footprint.

    Args:
        user: A User object.

     Returns:
        The user's carbon footprint in kilograms of carbon dioxide.
    """

    return user.get_carbon_footprint()
