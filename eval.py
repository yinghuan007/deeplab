python eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_65" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --eval_crop_size=360,480 \
    --dataset="camvid" \
    --checkpoint_dir='/Users/huanying/bai/dataset/CamVid/exp/camvid_train/train' \
    --eval_logdir='/Users/huanying/bai/dataset/CamVid/exp/camvid_train/eval' \
    --dataset_dir='/Users/huanying/bai/dataset/CamVid/tfrecord' \
    --max_number_of_evaluations=1
