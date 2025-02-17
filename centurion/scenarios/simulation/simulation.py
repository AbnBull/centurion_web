from collections import defaultdict
from datetime import datetime
from common.utilities.general_utilities import get_all_related_objects
from .simulate_pickups import simulate_pickups
from .simulate_deliveries import simulate_deliveries


def simulate_scenario(scenario):
    
    # TODO: gather data from cache
    # TODO: summarize orders so we can directly put data in the dashboard without queries
    # Gather data

    # setup simulation_data
    simulation_data = {
        'changed_instances': {}
    }

    
    # Get all related objects
    scenario_objects = get_all_related_objects(scenario)

    # sort by time and type
    event_collection = {}
    for event in scenario_objects:
        
        # create keys
        time_key = event.datetime().strftime("%Y%m%d%H%M")
        model_key = event._meta.model.__name__

        # create dict time entry if needed
        if time_key not in event_collection:
            event_collection[time_key] = {}
        
        # create dict model entry if needed
        if model_key not in event_collection[time_key]:
            print(f'adding {model_key} to dict')
            event_collection[time_key][model_key] = []

        # add event
        event_collection[time_key][model_key].append(event)

    # iterate objects
    for time_key in sorted(event_collection.keys()):
        
        # simulate deliveries
        if 'Delivery' in event_collection[time_key]:
            simulate_deliveries(deliveries=event_collection[time_key]['Delivery'], simulation_data=simulation_data)

        # simulate pickups
        if 'Pickup' in event_collection[time_key]:
            simulate_pickups(pickups=event_collection[time_key]['Pickup'], simulation_data=simulation_data)

        

    # save objects that changed
    for model_key in simulation_data['changed_instances']:
        for instance in simulation_data['changed_instances'][model_key]:
            instance.save()
            print(f'we saved {instance}')

    print('simulation complete!')