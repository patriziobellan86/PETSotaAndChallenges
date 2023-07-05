from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Goncalves-elements',
                  predictions_file_or_folder='Goncalves_elements.json',
                  output_results='results-Goncalves-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Goncalves-elements-strict',
                  predictions_file_or_folder='Goncalves_elements.json',
                  output_results='results-Goncalves-elements-strict',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Goncalves-relations',
                  predictions_file_or_folder='Goncalves_relations.json',
                  output_results='results-Goncalves-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Goncalves-relations-strict',
                  predictions_file_or_folder='Goncalves_relations.json',
                  output_results='results-Goncalves-relations-strict',
                  relax_window=0)
