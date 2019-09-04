# システム側
# ここでAIも実行する

# 数値要検討

# classたち

class village:
    """
    ムラを作るクラス
    インスタンスですべての村を管理
    村に関する情報をすべて変数に収める
    """

    def __init__(self, population):
        """
        村の初期状態を定義
        """
        self.population = population

        self.water = 0
        self.food_p = 0
        self.food_a_aqua = 0
        self.food_a_land = 0

    def add_population(self):
        """
        人口増加
        0～10歳の年代を増やす
        :return: なし
        """

    #

    def age_population(self):
        """
        定期的に年を取らせる
        年代をずらす

        書き直し

        :return:
        """

        for k, v in self.population.items():
            if v < 100 or v != 0:
                population[k + 5] = v

        population[0] = 0
        self.population.update(population)

    def die(self, generation, number):
        pass

    def set_health(self):
        pass

    # 外部からの呼び出しが行われる関数

    def spent(self):
        """
        時間の変化に合わせて必ず実行
        (5年)
        age_populationを実行後add_populationを実行
        最後に人口などといった諸データを返す
        """
        pass


class environment:
    """
    要求された地域の環境を作成するクラス
    """
    def __init__(self):
        pass

    def read(self):


    def soil(self, code):

        #土壌の管理コード　code

        #水              water
        #植物性食糧       food_p
        #水中動物性食料   food_a_aqua
        #陸上動物性食料   food_a_land

        if code == 0 or code == 2 or code == 9:
            pass

        elif code == 1:
            #水はけがよい土地
            self.water = -1
            self.food_a_land = 1

        elif code == 3:
            #湿地
            self.water = 1
            self.food_a_aqua = 1


    # 要求関数

    def request(self, ):
        pass




population = {i: 0 for i in range(0, 71, 5)}  # 0から70まで設定
