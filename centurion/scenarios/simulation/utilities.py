def add_instance_to_changed_types(instance, simulation_data):

    # get model name
    model_name = instance._meta.model.__name__

    # add model name to dict
    if model_name not in simulation_data['changed_instances']:
        simulation_data['changed_instances'][model_name] = []

    # add instance
    simulation_data['changed_instances'][model_name].append(instance)