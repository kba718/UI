import os
class Options():
    def __init__(self):
        super().__init__()
        self.Seed = 1234
        self.Epoch = 400
        self.Learning_Rate = 2e-4
        self.Batch_Size_Train = 32
        self.Batch_Size_Val = 32
        self.Patch_Size_Train = 256
        self.Patch_Size_Val = 256

        self.Input_Path_Train = './AWTD/train/input'
        self.Target_Path_Train = './AWTD/train/target'

        self.Input_Path_Val = './AWTD/test/RainDS-syn/input'
        self.Target_Path_Val = './AWTD/test/RainDS-syn/target'

        self.Dataset_Names = [
                              'FoggyCityscapes',
                              'RainCityscapes',
                              'RSCityscapes',
                              'SnowTrafficData',
                              'LowLightTrafficData',
                              'RainDS-syn'
        ]
        self.Path_Test = './AWTD/test'

        base_path = os.path.dirname(__file__)  # 即 MPMF-Net-master 所在目录
        self.MODEL_RESUME_PATH = os.path.join(base_path, 'weights', 'model_best.pth')


        self.Num_Works = 4
        self.CUDA_USE = True