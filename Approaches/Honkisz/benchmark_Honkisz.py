from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Honkisz-elements',
                  predictions_file_or_folder='Honkisz_elements.json',
                  output_results='results-Honkisz-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Honkisz-elements-strict',
                  predictions_file_or_folder='Honkisz_elements.json',
                  output_results='results-Honkisz-elements-strict',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Honkisz-relations',
                  predictions_file_or_folder='Honkisz_relations.json',
                  output_results='results-Honkisz-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Honkisz-relations-strict',
                  predictions_file_or_folder='Honkisz_relations.json',
                  output_results='results-Honkisz-relations-strict',
                  relax_window=0)
