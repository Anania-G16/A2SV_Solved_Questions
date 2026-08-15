class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([startGene])
        choices = ['A', 'C', 'G', 'T']
        count = 0
        visited = set([startGene])
        while queue:
            size = len(queue)
            for i in range(size):
                gene = queue.popleft()
                if gene == endGene:
                    return count
                for i in range(len(gene)):
                    for choice in choices:
                        if choice != gene[i]:
                            mutatedGene = gene[:i] + choice + gene[i+1:]
                            if mutatedGene in bank and mutatedGene not in visited:
                                visited.add(mutatedGene)
                                queue.append(mutatedGene)
            count += 1
        return -1
