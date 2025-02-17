from .utilities import add_instance_to_changed_types

def simulate_pickups(pickups, simulation_data):
    
    # generate attributes
    for pickup in pickups:

        # simulated attributes
        if pickup.simulated_attribute_hash() != pickup.saved_simulated_attribute_hash:
            print(f'bbefore generate country is {pickup.country}')
            pickup.generate_attributes()
            print(f'after generate country is {pickup.country}')
            add_instance_to_changed_types(instance=pickup, simulation_data=simulation_data)
