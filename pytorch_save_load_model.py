import torch
import shutil
import os

```
checkpoint = {
'epoch': epoch + 1,
'state_dict': model.state_dict(),
'optimizer': optimizer.state_dict(),
'best_test_acc': best_acc,
'train_acc_hist':train_acc_history,
'test_acc_hist': test_acc_history,
'train_loss_hist':train_loss_hist,
'test_loss_hist':test_loss_hist,
#save the random state such that restarting training from a certain epoch will get the same result as continuous training
'rng_state': torch.get_rng_state(),
'rand_rng_state':torch.random.get_rng_state(),
'cuda_rng_state':torch.cuda.get_rng_state()
}
```


def save_ckpt(ckpt, is_best = False, ckpt_dir = "./models/", best_model_dir = "./best_models/"):
    if not is_best:
        if not os.path.exists(ckpt_dir):
            os.makedirs(ckpt_dir)
        epoch = ckpt['epoch']
        f_path = ckpt_dir + 'checkpoint_' +str(epoch)+ '.pt'
        torch.save(ckpt, f_path)
    else:
        if not os.path.exists(best_model_dir):
            os.makedirs(best_model_dir)
        best_fpath = best_model_dir + 'best_model.pt'
        torch.save(ckpt, best_fpath)

def load_ckpt(ckpt_fpath, model, optimizer):
    checkpoint = torch.load(ckpt_fpath)
    model.load_state_dict(checkpoint['state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer'])
    # we set the random state as before to get reproducible results.
    torch.set_rng_state(checkpoint['rng_state'])
    torch.random.set_rng_state(checkpoint['rand_rng_state'])
    torch.cuda.set_rng_state(checkpoint['cuda_rng_state'])

    return model, optimizer, checkpoint['epoch'], checkpoint['best_test_acc'], checkpoint['train_acc_hist'], checkpoint['test_acc_hist'], checkpoint['train_loss_hist'], checkpoint['test_loss_hist']
