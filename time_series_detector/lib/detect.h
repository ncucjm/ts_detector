
#ifndef _DETECT_H
#define _DETECT_H

#include <inttypes.h>

#ifdef __cplusplus
extern "C"{
#endif

typedef struct {
    int* data_a;
    int* data_b;
    int* data_c;
    int len_a;
    int len_b;
    int len_c;
} ValueData;

typedef struct {
    double* data_a;
    double* data_b;
    double* data_c;
    int len_a;
    int len_b;
    int len_c;
} RateData;

enum TSD_ERR_CODE
{
    TSD_SUCCESS = 0,
    TSD_INVALID_HANDLER = -1,
    TSD_CHECK_PARAM_FAILED = -2,
    TSD_TIMESERIES_INIT_ERROR = -3
};

enum TSD_SAMPLE_RESULT
{
    TSD_NEGATIVE = 0,
    TSD_POSITIVE = 1
};

/*!
 * \load xgb model from xgb file
 * \param fname xgb file path and name
 * \return handle when success, NULL when failure happens
*/
void * load_model(const char *fname);

/*!
 * \Predict if the latest value is an outlier or not.
 * \param mhandle the handle of the xgb model
 * \param data the input data
 * \param sample_result:(1 denotes noraml, 0 denotes abnormal).
 * \return 0 when success, <0 when failure happens
*/
int value_predict(void * mhandle, ValueData* data, int* sample_result, float* prob);

/*!
 * \Predict if the latest value is an outlier or not.
 * \param mhandle the handle of the xgb model
 * \param data the input data
 * \param sample_result:(1 denotes noraml, 0 denotes abnormal).
 * \return 0 when success, <0 when failure happens
*/
int rate_predict(RateData* data, int* sample_result, float* prob);

#ifdef __cplusplus
}
#endif

#endif
