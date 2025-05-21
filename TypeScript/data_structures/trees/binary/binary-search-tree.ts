export class BinaryTreeNode<Type> {
	val: Type;
	left: BinaryTreeNode<Type> | null;
	right: BinaryTreeNode<Type> | null;
	constructor(
		val: Type,
		left?: BinaryTreeNode<Type> | null,
		right?: BinaryTreeNode<Type> | null
	) {
		this.val = val;
		this.left = left === undefined ? null : left;
		this.right = right === undefined ? null : right;
	}
}

export function BinaryTreeFromArray<Type>(
	arr: (Type | null)[]
): BinaryTreeNode<Type> | null {
	const construct = (index: number): BinaryTreeNode<Type> | null => {
		if (index >= arr.length || arr[index] == null) {
			return null;
		}

		return new BinaryTreeNode(
			arr[index],
			construct(2 * index + 1),
			construct(2 * index + 2)
		);
	};

	return construct(0);
}
