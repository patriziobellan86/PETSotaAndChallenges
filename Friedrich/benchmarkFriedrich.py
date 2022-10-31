from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Friedrich-elements',
                  predictions_file_or_folder='Friedrich_elements.json',
                  output_results='results-friedrich-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Friedrich-elements-sharp',
                  predictions_file_or_folder='Friedrich_elements.json',
                  output_results='results-friedrich-elements-sharp',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Friedrich-relations',
                  predictions_file_or_folder='Friedrich_relations.json',
                  output_results='results-friedrich-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Friedrich-relations-sharp',
                  predictions_file_or_folder='Friedrich_relations.json',
                  output_results='results-friedrich-relations-sharp',
                  relax_window=0)
