# Oxford-IIIT Pet

Практический проект классификации 37 пород кошек и собак.

Notebook-файлы расположены в порядке прохождения тем:

1. **01_data_pipeline.ipynb** — данные, split, transforms, Dataset/DataLoader.
2. **02_custom_cnn.ipynb** — собственная CNN.
3. **03_training_reliability.ipynb** — метрики, воспроизводимость, checkpoints и early stopping.
4. **04_transfer_learning.ipynb** — ResNet18, frozen backbone, обучение `fc`.
5. **05_fine_tuning.ipynb** — разморозка `layer4`, разные learning rate.
6. **06_augmentation.ipynb** — train-аугментации при детерминированной validation.
7. **07_error_analysis.ipynb** — метрики по породам, confusion matrix, частые пары ошибок и визуальный разбор.
8. **08_test_and_inference.ipynb** — финальная оценка на test и inference отдельного изображения.

## Принцип независимости

Каждый notebook содержит собственные импорты, seed/device setup, загрузку Oxford-IIIT Pet, создание необходимых split/DataLoader, модель и функции, нужные для конкретной темы. Можно открыть любой notebook отдельно в Google Colab и выполнить сверху вниз.

Checkpoint-файлы создаются самим notebook при необходимости; запуск предыдущего notebook не требуется.

## Итог проекта

- Лучшая validation accuracy после fine-tuning с аугментацией: **93.75%**.
- Лучшая validation macro-F1: **0.9377**.
- Финальная test accuracy: **89.53%**.
- Финальная test macro-F1: **0.8949**.
- Test top-3 accuracy: **98.64%**.
- Error analysis показал, что заметная часть ошибок связана с визуально похожими породами, в частности `Ragdoll` и `Birman`.

Тяжёлые визуальные outputs сохранены только в тех notebooks, где они являются частью изучаемой темы: подготовка данных, augmentation и error analysis. В остальных notebooks повторяющиеся галереи убраны, чтобы репозиторий оставался компактнее.
