from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Goncalves-elements',
                  predictions_file_or_folder='Goncalves_elements.json',
                  output_results='results-Goncalves-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Goncalves-elements-sharp',
                  predictions_file_or_folder='Goncalves_elements.json',
                  output_results='results-Goncalves-elements-sharp',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Goncalves-relations',
                  predictions_file_or_folder='Goncalves_relations.json',
                  output_results='results-Goncalves-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Goncalves-relations-sharp',
                  predictions_file_or_folder='Goncalves_relations.json',
                  output_results='results-Goncalves-relations-sharp',
                  relax_window=0)
