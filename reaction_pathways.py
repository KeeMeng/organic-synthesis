import random

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
		"N-Substituted_Amides, Nucleophillic Addition, + Acyl Chloride", 
		"Polyamides, Condensation Polymerisation, + Carboxylic Acid"]],
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
	["Amides", []],
	["Polyamides", []]
]


def synthesis(reagent, product):
	paths = []
	queue = [[reagent]]
	while queue:
		path = queue.pop(0)
		vertex = path[-1]
		if vertex == product:
			if paths:
				if len(paths[0]) == len(path):
					paths.append(path)
				else:
					break
			else:
				paths.append(path)
		for adjacent in adjacency_list[vertex]:
			if adjacent not in path:
				queue.append(path+[adjacent])


	return paths

def fancy_output1(path):
	output = ""
	for i in path[:-1]:
		output += vertices_name[i].replace("_", " ")
		output += " → "
	output += vertices_name[path[-1]].replace("_", " ")
	return output

def fancy_output2(path):
	output = ""
	for counter in range(len(path)-1):
		output += vertices_name[path[counter]].replace("_", " ")
		pos = adjacency_list[path[counter]].index(path[counter+1])
		output += f" ({vertices_info[path[counter]][1][pos].split(', ')[2]})"
		output += f"\n↓ {vertices_info[path[counter]][1][pos].split(', ')[1]}\n"
	output += vertices_name[path[-1]].replace("_", " ")

	return output


vertices_name = [i[0] for i in vertices_info]
v = len(vertices_name)
adjacency_list = [[vertices_name.index(j.split(", ")[0]) for j in vertices_info[i][1]] for i in range(v)]
allow_possible_only = True

print("0-Alkanes, 1-Alkenes, 2-Polyalkenes, 3-Halogenoalkanes, 4-Alcohols, 5-Ketones, 6-Amines, 7-Nitriles, 8-Grignard Reagents, 9-Aldehydes, 10-Hydroxynitriles, 11-Polyesters, 12-Esters, 13-N-Substituted Amides, 14-Carboxylic Acids, 15-Carboxylates, 16-Acyl Chlorides, 17-Amides, 18-Polyamides\n")
print("Enter homologous series ID or leave blank for a random choice")
reagent = input("Reagent: ")
product = input("Product: ")
reagent_random = not reagent
product_random = not product

reagent = random.randint(0, v-1) if reagent_random else int(reagent)
product = random.randint(0, v-1) if product_random else int(product)

paths = synthesis(reagent, product)
if allow_possible_only and (reagent_random or product_random):
	while len(paths) <= 1:
		if reagent_random:
			reagent = random.randint(0, v-1)
		if product_random:
			product = random.randint(0, v-1)
		paths = synthesis(reagent, product)

if paths:
	print(f"\nPath from {vertices_name[reagent].replace('_', ' ')}({reagent}) to {vertices_name[product].replace('_', ' ')}({product}): ")
	for counter in range(len(paths)):
		print(f"Path {counter}) {fancy_output1(paths[counter])}")
	while True:
		index = input("\nEnter path number for more details, or nothing to exit: ")
		if index:
			print(fancy_output2(paths[int(index)%len(paths)]))
		else:
			break
else:
	print(f"\n{vertices_name[reagent].replace('_', ' ')} cannot be synthesised into {vertices_name[product].replace('_', ' ')}")
