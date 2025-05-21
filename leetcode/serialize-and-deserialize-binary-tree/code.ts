import { BinaryTreeNode } from '../../TypeScript/data_structures/trees/binary/binary-search-tree';

class TreeNode extends BinaryTreeNode<number> {}

/*
 * Encodes a tree to a single string.
 */

const DELIM = '|';
const NULL = '#';
export function serialize(root: TreeNode | null): string {
	let serializeNode = (node: TreeNode | null): string => {
		if (node != null) {
			return `${DELIM}${node.val}${serializeNode(node.left)}${serializeNode(
				node.right
			)}`;
		} else {
			return `${DELIM}${NULL}`;
		}
	};

	return serializeNode(root).substring(DELIM.length);
}

/*
 * Decodes your encoded data to tree.
 */
export function deserialize(data: string): TreeNode | null {
	let start: number;
	let end: number = -1;
	let val: string;

	let construct = (): TreeNode | null => {
		start = end + 1;
		end = data.indexOf(DELIM, start);

		if (end < 0) {
			if (data.length <= start) {
				// Ended with Delimiter -> No more Data
				return null;
			} else if (start == data.length - 1) {
				// No ending delimiter -> last value
				val = data[data.length - 1];
			} else {
				// Invalid serialization
				throw new Error('Invalid Serialization');
			}
		} else {
			//Read current value from between delimiters
			val = data.substring(start, end);
		}

		if (val == NULL) {
			return null;
		} else {
			return new TreeNode(parseInt(val), construct(), construct());
		}
	};

	return construct();
}
