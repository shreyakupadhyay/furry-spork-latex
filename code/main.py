import json
import min_dfa
import reduction
import generate_code

if __name__ == "__main__":
	equi_blocks_list = min_dfa.main()
	reduced_json = reduction.main(equi_blocks_list)
	generate_code.main(json.dumps(reduced_json))