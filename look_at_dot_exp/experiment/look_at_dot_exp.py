import random
import pandas as pd
import pylsl as lsl
from psychopy import core, parallel, visual

# create a window
win = visual.Window([800, 600], fullscr=True, monitor="testMonitor", units="deg", color=(-1, -1, -1), useFBO=False)

subject_id = '001'
num_images = 240
options = [f'figures_decoding_exp/fig{i}.png' for i in range(num_images)]
info = lsl.StreamInfo(name='Trigger Stream', type='Markers', channel_count=1, channel_format='int32', source_id='uniqueid12345')
outlet = lsl.StreamOutlet(info, chunk_size=0)

# Experiment Flow Function    
def main():
    slidePic0 = visual.ImageStim(win, image="look_at_dot.png",  units='norm', size=[2,2], interpolate = True)
    slidePic0.draw()
    win.update()
    core.wait(5)
    random.shuffle(options)
    pd.DataFrame(options).to_csv(f'shuffle_order_{subject_id}.csv')
    for image in options:
        parallel.setData(0)
        slidePic1 = visual.ImageStim(win, image="fixation.jpg",  units='norm', size=[2,2], interpolate = True)
        slidePic1.draw()
        win.update()
        core.wait(0.3)
        parallel.setPin(2, 1)  # sets just this pin to be high
        slidePic2 = visual.ImageStim(win, image=image,  units='norm', size=[2,2], interpolate = True)
        slidePic2.draw()
        win.update()
        core.wait(1)       
    win.close()


main()
