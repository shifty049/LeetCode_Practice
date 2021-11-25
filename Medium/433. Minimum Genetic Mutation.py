class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        string_lst = ['A', 'C', 'G', 'T']
        
        queue = [start]
        
        bank_set =  set(bank)
       
        mut_num = 0
        
        while queue:
            new_queue = []
            mut_num += 1
            
            for g in queue:
                for idx, wd in enumerate(g):
          
                    for sw in string_lst:

                        if sw != wd:
                            new_gene = g[:idx] + sw + g[idx + 1:]
                           
                            if new_gene in bank_set:
                                if new_gene == end:
                                    return mut_num
                
                                bank_set.remove(new_gene)                       
                                new_queue.append(new_gene)
                    
            queue = new_queue
        return -1

#Runtime: 28 ms, faster than 85.76% of Python3 online submissions for Minimum Genetic Mutation.
#Memory Usage: 14.3 MB, less than 32.80% of Python3 online submissions for Minimum Genetic Mutation.
#Fu-Ti, Hsu 
#shifty049@gmail.com