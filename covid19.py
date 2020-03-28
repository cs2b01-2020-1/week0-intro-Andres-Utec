from difflib import SequenceMatcher
#results_percent.append(SequenceMatcher(None, genome, genomes).ratio())

def compare_genomes(genome, list_genomes):
    results_percent = []
    size_genome = len(genome)
    for genomes in list_genomes:
        equality = 0
        temp = 0
        for genome_char in genome:
            if genomes[temp] == genome_char:
                equality+=1
            elif genome == genomes:
                results_percent.append(1.0)
                break
            else:
                continue
            temp+=1
        results_percent.append(round(float(equality)/float(size_genome), 2))
    return results_percent

def display_result(percent_results, name_txt):
    print( " " +"_"*67 + " ")
    print("{} {} {} {} {}".format("|"," "*28, "Covid-19", " " *27,"|"))
    print("|"+ "_"*67 +"|")
    i = 0
    print("|{} | {} | {} | {} | {} | {} |".format(" "*11,name_txt[0][:8],name_txt[1][:8],name_txt[2][:8],name_txt[3][:8],name_txt[4][:8]))
    print("|"+ "_"*67 +"|")
    for results in percent_results:
        print("|  {}  |   {:.2f}   |   {:.2f}   |   {:.2f}   |   {:.2f}   |   {:.2f}   |".format(name_txt[i][:8],results[0],results[1],results[2],results[3],results[4]))
        print("|" +"_"*67 +"|")
        i+=1


file_txt = ["AY274119.txt","AY278488.2.txt","MN908947.txt","MN988668.txt","MN988669.txt"]
list_genomes = []
for file in file_txt:
    f = open(file, "r")
    f.readline()
    list_genomes.append(f.read())
results = []
for genomes in list_genomes:
    results.append(compare_genomes(genomes, list_genomes))

display_result(results, file_txt)
