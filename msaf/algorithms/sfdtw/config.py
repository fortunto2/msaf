"""Config for the Structural Features algorithm."""
import os

# Serra params
config = {
    "M_gaussian"    : 20,
    "m_embedded"    : 1,
    "k_nearest"     : 0.03,
    "Mp_adaptive"   : 28,
    "offset_thres"  : 0.09,
    "recplot_type"  : "predict",
    "recplots_dir"  : "/home/uri/Projects/similarity_classification/recplots",
    "features_dir"  : "/home/uri/Projects/similarity_classification/features",
    "model"         : os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              "models", "similarity_model_isophonics.pickle")
    #"model"         : os.path.join(os.path.dirname(os.path.realpath(__file__)),
                              #"models", "similarity_model_salami.pickle")
    #"model"         : None

    # For framesync features
    #"M_gaussian"    : 100,
    #"m_embedded"    : 3,
    #"k_nearest"     : 0.06,
    #"Mp_adaptive"   : 100,
    #"offset_thres"  : 0.01
}

algo_id = "sfdtw"
is_boundary_type = True
is_label_type = False
