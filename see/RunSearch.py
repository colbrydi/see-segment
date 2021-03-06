import argparse
import sys
import matplotlib.pylab as plt
import imageio
from see import GeneticSearch, Segmentors



def readfpop(fpop_file):
    fid_out= open(f"{input_file}.txt","r")
    

def continuous_search(input_file, 
                      input_mask, 
                      startfile='',
                      checkpoint='checkpoint.txt',
                      best_mask_file="temp_mask.png", 
                      pop_size=10):
    
    img = imageio.imread(input_file)
    gmask = imageio.imread(input_mask)

    fid_out= open(f"{input_file}.txt","w+")
    
    #TODO: Read this file in and set population first
    
    #Run the search
    my_evolver = GeneticSearch.Evolver(img, gmask, pop_size=pop_size)

    best_fitness=2.0
    iteration = 0
 
    while(best_fitness > 0.0):
        print(f"running {iteration} iteration")
        if(startfile):
            population = my_evolver.run(ngen=1, startfile=None)
            startfile = None
        else:
            population = my_evolver.run(ngen=1)
            
        #Get the best algorithm so far
        params = my_evolver.hof[0]

        #Generate mask of best so far.
        seg = Segmentors.algoFromParams(params)
        mask = seg.evaluate(img)
        
        fitness = Segmentors.FitnessFunction(mask, gmask)[0]
        if (fitness < best_fitness):
            best_fitness = fitness
            print(f"\n\n\n\nIteration {iteration} Finess Improved to {fitness}")
            my_evolver.writepop(population, filename="checkpoint.pop")
            #imageio.imwrite(best_mask_file,mask);
            fid_out.write(f"[{iteration}, {fitness}, {params}]\n")
            fid_out.flush(); 
            ###TODO Output [fitness, seg]
        iteration += 1

def geneticsearch_commandline():
    """Rename Instructor notebook using git and fix all
    student links in files."""
    parser = argparse.ArgumentParser(description='rename notebook')

    parser.add_argument('input_file', help=' input image')
    parser.add_argument('input_mask', help=' input Ground Truthe Mask')
    parser.add_argument('start_pop', nargs='?', help=' Population File used in transfer learning')
    
    args = parser.parse_args()
    
    print("HELLO WORLD DIRK")
    print('\n\n')
    print(args)
    print('\n\n')
    
    continuous_search(args.input_file, args.input_mask, args.start_pop);

#     #Multilabel Array Example
#     img = imageio.imread(args.input_file)
#     gmask = imageio.imread(args.input_mask)

#     #Run the search
#     my_evolver = GeneticSearch.Evolver(img, gmask, pop_size=10)
#     population = my_evolver.run(ngen=5)
    
#     #Get the best algorithm so far
#     params = my_evolver.hof[0]
#     print('Best Individual:\n', params)
    
#     #Generate mask of best so far.
#     seg = Segmentors.algoFromParams(params)
#     mask = seg.evaluate(img)
    
#     imageio.imwrite('./temp_mask.png',mask);
    
    
if __name__ == "__main__":
    geneticsearch_commandline()
