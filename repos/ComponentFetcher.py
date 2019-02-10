from Models import Component


def get_components(component_type: Component):
	component_file_paths = {
		"ShipType": "ShipTypes.txt",
		"Computer": "Computers.txt",
		"ImpulseEngine": "ImpulseEngines.txt",
		"JumpDrive": "JumpDrives.txt",
		"Radar": "Radars.txt"
	}
	components = {}
	
	fhand = open(component_file_paths[component_type.name])
	
	for line in fhand:
		stats = line.split(",")
		to_add = component_type.__init__(*stats)
		components[to_add.id] = to_add
	
	return components
