python vis.py \
    --logtostderr \
    --vis_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --vis_crop_size=360,480 \
    --dataset="camvid" \
    --colormap_type="pascal" \
    --checkpoint_dir='/Users/huanying/bai/dataset/CamVid/exp/camvid_train/train' \
    --vis_logdir='/Users/huanying/bai/dataset/CamVid/exp/camvid_train/vis' \
    --dataset_dir='/Users/huanying/bai/dataset/CamVid/tfrecord'
