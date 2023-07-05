from petbenchmarks.benchmarks import BenchmarkApproach

print('elements')
BenchmarkApproach(approach_name='Friedrich-elements',
                  predictions_file_or_folder='Friedrich_elements.json',
                  output_results='results-friedrich-elements',
                  relax_window=1)
BenchmarkApproach(approach_name='Friedrich-elements-strict',
                  predictions_file_or_folder='Friedrich_elements.json',
                  output_results='results-friedrich-elements-strict',
                  relax_window=0)

print('relations')
BenchmarkApproach(approach_name='Friedrich-relations',
                  predictions_file_or_folder='Friedrich_relations.json',
                  output_results='results-friedrich-relations',
                  relax_window=1)
BenchmarkApproach(approach_name='Friedrich-relations-strict',
                  predictions_file_or_folder='Friedrich_relations.json',
                  output_results='results-friedrich-relations-strict',
                  relax_window=0)
