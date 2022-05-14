vertices_info = [
	["Alkanes", [
		"Alkenes, Cracking, + Heat", 
		"Halogenoalkanes, Free Radical Substitution, + X2 + UV Light"]],
	["Alkenes", [
		"Alkanes, Hydrogenation/Reduction, + H2 + Ni + 150ºc", 
		"Polyalkenes, Polymerisation, + High Pressure + Catalyst", 
		"Halogenoalkanes, Electrophillic Addition, + HX/H2", 
		"Alcohols, Hydration/Addition/Oxidation, + H2O + c.H3PO4 + 300ºc + 60-70atm"]],
	["Polyalkenes", []],
	["Halogenoalkanes", [
		"Alkenes, Elimination, + KOH + Ethanol Solvent + 60ºc", 
		"Alcohols, Nucleophillic Substitution, + NaOh + 35ºc", 
		"Amines, Nucleophillic Substitution, + Excess NH3 + Ethanol Solvent + Heat", 
		"Nitriles, Nucleophillic Substitution, + KCN + HCN + Ethanol Solvent", 
		"Grignard_Reagents, Oxidative Addition, + Mg + Dry Ether + Reflux"]],
	["Alcohols", [
		"Alkenes, Elimination/Dehydration, + c.H3PO4 + 180ºc", 
		"Halogenoalkanes, Oxidation, + PCl5 or KBr + H2SO4 or 2P + 3I2", 
		"Ketones, Oxidation, + Acidified K2Cr2O7", 
		"Aldehydes, Oxidation, + Acidified K2Cr2O7", 
		"Esters, Esterification/Condensation Polymerisation, + Alcohol/Carboxylic Acid + H2SO4 + Heat or Acyl Chloride"]],
	["Ketones", [
		"Alcohols, Reduction, + LiAlH4 + Dry Ether", 
		"Hydroxynitriles, Nucleophillic Addition, + KCN + HCN + Ethanol Solvent"]],
	["Amines", [
		"N-Substituted_Amides, Nucleophillic Addition, + Acyl Chloride"]],
	["Nitriles", [
		"Amines, Reduction, + LiAlH4 + Dry Ether or H2 + Ni", 
		"Carboxylic_Acids, Hydrolysis, + H+ + Reflux or OH- + Reflux + Acid Workup"]],
	["Grignard_Reagents", [
		"Alcohols, Nucleophillic Addition, + Carbonyl Compound + Dry Ether", 
		"Carboxylic_Acids, Nucleophillic Addition, + CO2 + Acid Workup"]],
	["Aldehydes", [
		"Alcohols, Reduction, + LiAlH4 + Dry Ether", 
		"Hydroxynitriles, Nucleophillic Addition, + KCN + HCN + Ethanol Solvent, + KCN + HCN + Ethanol Solvent", 
		"Carboxylic_Acids, Oxidation, + Acidified K2Cr2O7"]],
	["Hydroxynitriles", [
		"Carboxylic_Acids, Hydrolysis, + H+ + Heat or OH- + Heat + Acid Workup"]],
	["Polyesters", []],
	["Esters", [
		"Alcohols, Hydrolysis, + H2O + H2SO4 + Reflux", 
		"Polyesters, Condensation Polymerisation, + Catalyst", 
		"Carboxylic_Acids, Acidic Hydrolysis, + H2O + H2SO4 + Reflux", 
		"Carboxylates, Alkaline Hydrolysis, + H2O + NaOH + Reflux"]],
	["N-Substituted_Amides", []],
	["Carboxylic_Acids", [
		"Aldehydes, Reduction, + LiAlH4 + Dry Ether", 
		"Esters, Esterification, + Alcohol + H2SO4 + Heat", 
		"Carboxylates, Neutralisation, + OH-", 
		"Acyl_Chlorides, Chlorination, + PCl5"]],
	["Carboxylates", [
		"Carboxylic_Acids, Recombination, + H+ + Heat"]],
	["Acyl_Chlorides", [
		"Esters, Nucleophillic Addition, + Alcohol", 
		"N-Substituted_Amides, Nucleophillic Addition, + Amine", 
		"Carboxylic_Acids, Nucleophillic Substitution, + H2O", 
		"Amides, Nucleophillic Addition, + NH3"]],
	["Amides", [
		"Polyamides, Condensation Polymerisation, + Carboxylic Acid"]],
	["Polyamides", []],
	["Amino_Acids", [
		"Polyamides, Condensation Polymerisation, + Catalyst"]]
]

vertices_name = [i[0] for i in vertices_info]
v = len(vertices_name)

adjacency_list = [[vertices_name.index(j.split(", ")[0]) for j in vertices_info[i][1]] for i in range(v)]


def synthesis(reagent, product):
	output = ""

	queue = [[reagent]]
	while queue:
		path = queue.pop(0)
		vertex = path[-1]
		if vertex == product:
			break
		for adjacent in adjacency_list[vertex]:
			if adjacent not in path:
				queue.append(path+[adjacent])


	if path[-1] != product:
		output += f"{vertices_name[reagent].replace('_', ' ')} cannot be synthesised into {vertices_name[product].replace('_', ' ')}"

	else:
		output += f"Path from {vertices_name[reagent].replace('_', ' ')} to {vertices_name[product].replace('_', ' ')}: \n"
		for counter in range(len(path)-1):
			output += vertices_name[path[counter]].replace("_", " ")
			pos = adjacency_list[path[counter]].index(path[counter+1])
			output += f" ({vertices_info[path[counter]][1][pos].split(', ')[2]})"
			output += f"\n↓ {vertices_info[path[counter]][1][pos].split(', ')[1]}\n"
		
		output += vertices_name[path[-1]].replace("_", " ")

		# print(f"\nPath length: {len(path)-1}")
		# print("Raw path:", path)

	return output

reagent = int(input("Reagent: "))
product = int(input("Product: "))

print(synthesis(reagent, product))
