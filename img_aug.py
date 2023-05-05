import Augmentor
import os
def makedir(path):
    '''
    if path does not exist in the file system, create it
    '''
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    datasets_root_dir = '/home/robin/data/cub200_cropped/'
    dir = datasets_root_dir + 'train_cropped/'
    target_dir = datasets_root_dir + 'train_cropped_augmented/'

    makedir(target_dir)
    folders = [os.path.join(dir, folder) for folder in next(os.walk(dir))[1]]
    target_folders = [os.path.join(target_dir, folder) for folder in next(os.walk(dir))[1]]

    for i in range(len(folders)):
        fd = folders[i]
        tfd = target_folders[i]
        # rotation
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.rotate(probability=1, max_left_rotation=15, max_right_rotation=15)
        p.flip_left_right(probability=0.5)
        for i in range(10):
            p.process()
        del p
        # skew
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.skew(probability=1, magnitude=0.2)  # max 45 degrees
        p.flip_left_right(probability=0.5)
        for i in range(10):
            p.process()
        del p
        # shear
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.shear(probability=1, max_shear_left=10, max_shear_right=10)
        p.flip_left_right(probability=0.5)
        for i in range(10):
            p.process()
        del p
        # random_distortion
        #p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        #p.random_distortion(probability=1.0, grid_width=10, grid_height=10, magnitude=5)
        #p.flip_left_right(probability=0.5)
        #for i in range(10):
        #    p.process()
        #del p

if __name__ == "__main__":
    main()

# Processing <PIL.Image.Image image mode=RGB size=394x282 at 0x7F93A67D8CD0>: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 30/30 [00:00<00:00, 1445.75 Samples/s]
# Processing <PIL.Image.Image image mode=RGB size=206x118 at 0x7F93AD1A48E0>:  50%|███████████████████████████████████████████████████████████████████                                                                   | 15/30 [00:00<00:00, 740.97 Samples/s]
# Traceback (most recent call last):
#   File "/home/robin/github/forked/ProtoPNet/img_aug.py", line 52, in <module>
#     main()
#   File "/home/robin/github/forked/ProtoPNet/img_aug.py", line 27, in main
#     p.process()
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/site-packages/Augmentor/Pipeline.py", line 391, in process
#     self.sample(0, multi_threaded=True)
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/site-packages/Augmentor/Pipeline.py", line 364, in sample
#     for result in executor.map(self, augmentor_images):
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/concurrent/futures/_base.py", line 609, in result_iterator
#     yield fs.pop().result()
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/concurrent/futures/_base.py", line 439, in result
#     return self.__get_result()
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
#     raise self._exception
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/concurrent/futures/thread.py", line 58, in run
#     result = self.fn(*self.args, **self.kwargs)
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/site-packages/Augmentor/Pipeline.py", line 105, in __call__
#     return self._execute(augmentor_image)
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/site-packages/Augmentor/Pipeline.py", line 233, in _execute
#     images = operation.perform_operation(images)
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/site-packages/Augmentor/Operations.py", line 851, in perform_operation
#     augmented_images.append(do(image))
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/site-packages/Augmentor/Operations.py", line 843, in do
#     image = image.crop((int(round(E)), int(round(A)), int(round(X - E)), int(round(Y - A))))
#   File "/home/robin/anaconda3/envs/img_aug/lib/python3.9/site-packages/PIL/Image.py", line 1227, in crop
#     raise ValueError(msg)
# ValueError: Coordinate 'lower' is less than 'upper'