from .utilities import add_instance_to_changed_types

def simulate_deliveries(deliveries, simulation_data):
    
    # generate attributes
    for delivery in deliveries:

        # simulated attributes
        if delivery.simulated_attribute_hash() != delivery.saved_simulated_attribute_hash:
            print(f'bbefore generate country is {delivery.country}')
            delivery.generate_attributes()
            print(f'after generate country is {delivery.country}')
            add_instance_to_changed_types(instance=delivery, simulation_data=simulation_data)
