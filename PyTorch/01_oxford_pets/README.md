# Oxford-IIIT Pet

Практический проект классификации 37 пород кошек и собак.

Notebook-файлы расположены в порядке прохождения тем:

1. **01_data_pipeline.ipynb** — данные, split, transforms, Dataset/DataLoader.
2. **02_custom_cnn.ipynb** — собственная CNN.
3. **03_training_reliability.ipynb** — метрики, воспроизводимость, checkpoints и early stopping.
4. **04_transfer_learning.ipynb** — ResNet18, frozen backbone, обучение `fc`.
5. **05_fine_tuning.ipynb** — разморозка `layer4`, разные learning rate.
6. **06_augmentation.ipynb** — train-аугментации при детерминированной validation.
7. **07_error_analysis.ipynb** — заготовка следующей темы.
8. **08_test_and_inference.ipynb** — заготовка финальной темы.

## Принцип независимости

Каждый содержательный notebook содержит собственные импорты, seed/device setup, загрузку Oxford-IIIT Pet, создание split/DataLoader и необходимые функции. Можно открыть любой notebook отдельно в Google Colab и выполнить сверху вниз.

Checkpoint-файлы создаются самим notebook при необходимости; запуск предыдущего notebook не требуется.
