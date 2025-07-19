from analyzer.strength_checker import analyze_strength
def generate_recommendations(Analyzer_output:dict) -> list:
    recommendations = []
    if Analyzer_output["length"]<8:
        recommendations.append("Use atleast 8 characters for your password")
    if not Analyzer_output["has_uppercase"] :
        recommendations.append("Add uppercase character for generating strong password")
    if not Analyzer_output["has_lowercase"]:
        recommendations.append("Add lowercase character for generating strong password")
    if not Analyzer_output["has_digits"]:
        recommendations.append("Add some Digits for generating strong password")
    if not Analyzer_output["has_special_characters"]:
        recommendations.append("Add some Special characters for generating strong password")
    if Analyzer_output["is_common"]:
        recommendations.append("Added password is commonly used please another password")
    if not recommendations:
        recommendations.append("Your password looks strong! great work!")

    return recommendations
        
