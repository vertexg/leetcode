class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [dict() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        self.buckets[self._hash(key)][key] = value

    def get(self, key: int) -> int:
        return self.buckets[self._hash(key)].get(key, -1)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            del bucket[key]

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]


class MyHashMap:

    def __init__(self):
        # ハッシュテーブルのサイズ（素数が望ましい）
        self.size = 1009
        # バケットを作成（各バケットはキーと値のペアのリスト）
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # ハッシュ関数：key を size で割った余り
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # ハッシュ値（バケットのインデックス）を計算
        index = self._hash(key)
        bucket = self.buckets[index]

        # バケット内を走査して、同じキーがあるか確認
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # キーが既にあれば、値を更新
                bucket[i] = (key, value)
                return

        # キーがなければ、新しく追加
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]

        # バケット内を走査して、キーを探す
        for k, v in bucket:
            if k == key:
                return v  # 見つかれば値を返す

        return -1  # 見つからなければ -1 を返す

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        # バケット内を走査して、キーを探して削除
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # 削除
                return
https://leetcode.com/problems/design-hashmap/
