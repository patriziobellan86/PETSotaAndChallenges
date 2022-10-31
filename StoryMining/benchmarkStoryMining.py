from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='StoryMining-elements',
                  predictions_file_or_folder='StoryMining_process_elements.json',
                  output_results='results-storymining-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='StoryMining-elements-sharp',
                  predictions_file_or_folder='StoryMining_process_elements.json',
                  output_results='results-storymining-elements-sharp',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='StoryMining-relations',
                  predictions_file_or_folder='StoryMining_process_relations.json',
                  output_results='results-storymining-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='StoryMining-relations-sharp',
                  predictions_file_or_folder='StoryMining_process_relations.json',
                  output_results='results-storymining-relations-sharp',
                  relax_window=0)
